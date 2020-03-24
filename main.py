# Performs target search on provided images
# main.py handles io to bash
import argparse
import socket
import target_search

# Create argparse object:
parser = argparse.ArgumentParser()
parser.add_argument('image_in', type=str,
                    help='The input file. Must be .jpg')
parser.add_argument('-v', '--verbose', action='storeTrue',
                    help='Optional. True to display intermediate steps for debugging')
parser.add_argument('-p','--publish', type=str,
                    help='Optional. Publish to provided url, as specified here: https://github.com/auvsi-suas/interop#upload-objects.')

# TODO: check for bad input
args = parser.parse_args()
filename = args.image_in
verbose = args.verbose
publish = args.publish


if verbose:
    print('Verbosity Enabled')

out_list = target_search.getTargets(filename, verbose)

if verbose:
    for out_obj in out_list:
        print('Image file generated at {}'.format(out_obj['img_path']))
        print('Image data generated at {}'.format(out_obj['json_path']))
