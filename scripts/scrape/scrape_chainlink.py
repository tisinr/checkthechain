#!/usr/bin/env python3

import argparse

from fei.data.protocols import chainlink_data


parser = argparse.ArgumentParser()
parser.add_argument('--dry', action='store_true')
args = parser.parse_args()
dry = args.dry


save_feeds = [
    'ETH_USD',
    'FEI_ETH',
    'FRAX_ETH',
    'DAI_USD',
    'SUSD_ETH',
    'RAI_ETH',
]


if dry:
    print('!! [DRY RUN] !!')
print('scraping chainlink feeds:')
for feed in save_feeds:
    print('-', feed)
print()


for feed in save_feeds:
    print('saving feed:', feed)
    print()
    chainlink_data.save_feed_to_present(feed=feed, dry=dry)
    print()
    print()

print('done with all feeds')
if dry:
    print('!! [DRY RUN] !!')
