from flask import Flask, jsonify, request
from lib import currency_manager
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="Port.", type=int)
    return parser.parse_args()


if __name__ == '__main__':
    app = Flask(__name__)
    parsed_args = parse_args()

    @app.route('/currency_converter')
    def convert():
        args = request.args
        c = currency_manager.CurrencyManager(
            args.get("from"), args.get("to"), args.get("amount"))

        if not args.get("to"):
            return jsonify(c.convert_all())

        return jsonify(c.convert())

    app.run(port=parsed_args.port)
