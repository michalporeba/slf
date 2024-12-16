import json
import json_stream
from json_stream.dump import JSONStreamEncoder, default


def stream_json_array(path):
    with open(path, 'r') as f:
        data = json_stream.load(f)
        for d in data.persistent():
            yield dict(d)


def process_awards(limit=10):
    for award in stream_json_array('data/awards.json'):
        print(type(award))
        print(award)
        print()
        break


if __name__ == '__main__':
    process_awards(1)
