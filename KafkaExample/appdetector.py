import time
from flask import Flask, Response, stream_with_context, render_template, json, url_for
import jinja2

from kafka import KafkaConsumer
from KafkaExample import *

app = Flask(__name__)
my_loader = jinja2.ChoiceLoader([app.jinja_loader,jinja2.FileSystemLoader('/KafkaExample/templates'),])
app.jinja_loader = my_loader

def stream_template(template_name, **context):
    print('template name =',template_name)
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.enable_buffering(5)
    return rv

def is_suspicious(transaction: dict) -> bool:
    """Determine wether a transaction is suspicious."""
    return transaction["amount"] >= 900


@app.route('/')
def index():
    def g():
        consumer = KafkaConsumer(
            TRANSACTIONS_TOPIC
            , bootstrap_servers=KAFKA_BROKER_URL
            , value_deserializer=lambda value: json.loads(value)
            ,
        )
        for message in consumer:
            transaction: dict = message.value
            topic = FRAUD_TOPIC if is_suspicious(transaction) else LEGIT_TOPIC
            print(topic, transaction)  # DEBUG
            yield topic, transaction

    return Response(stream_template('index.html', title='Fraud Detector / Kafka',data=g()))

if __name__ == "__main__":
   app.run(host="localhost" , debug=True)
