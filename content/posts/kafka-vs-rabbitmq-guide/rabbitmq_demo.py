import argparse
import json
import os
from pathlib import Path

import pika


QUEUE = "orders-demo"


def main():
    parser = argparse.ArgumentParser(description="Local RabbitMQ publish/ACK demo")
    parser.add_argument("action", choices=["publish", "consume"])
    args = parser.parse_args()

    messages = Path(__file__).with_name("messages.jsonl").read_text().splitlines()
    for message in messages:
        json.loads(message)

    credentials = pika.PlainCredentials(
        os.getenv("RABBITMQ_USER", "bloglab"),
        os.getenv("RABBITMQ_PASSWORD", "local-lab-only"),
    )
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="127.0.0.1", credentials=credentials, socket_timeout=10
        )
    )
    try:
        channel = connection.channel()
        channel.queue_declare(
            queue=QUEUE, durable=True, arguments={"x-queue-type": "classic"}
        )

        if args.action == "publish":
            channel.confirm_delivery()
            for message in messages:
                channel.basic_publish(
                    exchange="",
                    routing_key=QUEUE,
                    body=message.encode("utf-8"),
                    properties=pika.BasicProperties(
                        delivery_mode=2, content_type="application/json"
                    ),
                    mandatory=True,
                )
                print(f"PUBLISHED {message}", flush=True)
        else:
            for _ in messages:
                method, _, body = channel.basic_get(queue=QUEUE, auto_ack=False)
                if method is None:
                    raise SystemExit("Queue is empty. Publish three messages first.")
                event = json.loads(body)
                print(f"PROCESSED {event['order_id']}: {body.decode()}", flush=True)
                channel.basic_ack(delivery_tag=method.delivery_tag)
                print(f"ACK {event['order_id']}", flush=True)

        remaining = channel.queue_declare(queue=QUEUE, passive=True).method.message_count
        print(f"READY {remaining}", flush=True)
    finally:
        connection.close()


if __name__ == "__main__":
    main()
