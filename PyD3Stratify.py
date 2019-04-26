import sys
import csv
import json


class PyD3Stratify(object):
    def __init__(self):
        pass

    def stratify(self, args):
        with open(args['i'], 'r') as input:
            headers = self._get_headers(input)
            reader = list(csv.DictReader(input, fieldnames=headers))

            lookup = self._get_lookup(args['lookup'])\
                if 'lookup' in args else None
            headers = args['headers'] if 'headers' in args else headers
            root = args['root'] if 'root' in args else None

            processed = self._process(reader, headers, root, lookup)

            self._export(args['o'], processed)

    def _get_headers(self, input):
        reader = csv.reader(input)
        headers = next(reader)
        return headers

    def _get_lookup(self, lookup):
        with open(lookup, 'r') as f:
            result = json.load(f)
        return result

    def _process(self, reader, headers, root, lookup):
        processed = []
        parents = set()
        leaves = {}
        header_length = len(headers)

        if root:
            processed.append({'name': root, 'parent': ''})

        for row in reader:
            current = root

            for i in range(header_length):
                key = headers[i]
                pre = current
                current += '->' + lookup[row[key]]\
                    if lookup and row[key] in lookup else '->' + row[key]

                if i != header_length - 1 and current in parents:
                    continue  # append each parent for only once

                if i == header_length - 1:
                    if current in leaves:
                        leaves[current]['size'] += 1
                    else:
                        leaf = {
                            'name': current,
                            'parent': pre,
                            'size': 1
                        }
                        leaves[current] = leaf
                else:
                    processed.append({
                        'name': current,
                        'parent': pre,
                        'size': None
                    })

                if i != header_length - 1:
                    parents.add(current)

        processed += leaves.values()

        return processed

    def _export(self, output_file, data):
        with open(output_file, 'w') as output:
            json.dump(data, output)


def print_usage_and_exit():
    print('Lack of arguments: input or output')
    print('Usage: python3 PyD3Stratify.py -i <input_file> -o <output_file>')
    print('Optional: --headers "<item>,<item>,<item>" --root <root_name> --lookup <lookup_file>')
    exit(1)


if __name__ == '__main__':
    args = {}

    # parsing arguments
    length = len(sys.argv)
    for i in range(length):
        if i % 2 == 0:
            continue
        elif i + 1 < length:
            if sys.argv[i] in ['-i', '-o', '--root', '--lookup']:
                key = sys.argv[i].replace('-', '')
                args[key] = sys.argv[i + 1]
            elif sys.argv[i] == '--headers':
                args['headers'] = sys.argv[i + 1].split(',')

    # input and output are requirements
    if args['i'] == '' or args['o'] == '':
        print_usage_and_exit()

    pds = PyD3Stratify()
    pds.stratify(args)
