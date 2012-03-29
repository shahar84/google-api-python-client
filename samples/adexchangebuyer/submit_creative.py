#!/usr/bin/python
#
# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example illustrates how to submit a new creative for its verification.

Tags: creatives.insert
"""

__author__ = 'david.t@google.com (David Torres)'

import pprint
import sys
import gflags
from oauth2client.client import AccessTokenRefreshError
import sample_utils

# Declare command-line flags, and set them as required.
gflags.DEFINE_string('account_id', None,
                     'The ID of the account to which submit the creative',
                     short_name='a')
gflags.MarkFlagAsRequired('account_id')
gflags.DEFINE_string('adgroup_id', None,
                     'The pretargeting adgroup id that this creative will be '
                     'associated with',
                     short_name='g')
gflags.MarkFlagAsRequired('adgroup_id')
gflags.DEFINE_string('buyer_creative_id', None,
                     'A buyer-specific id identifying the creative in this ad',
                     short_name='c')
gflags.MarkFlagAsRequired('buyer_creative_id')


def main(argv):
  sample_utils.process_flags(argv)
  account_id = gflags.FLAGS.account_id
  adgroup_id = gflags.FLAGS.adgroup_id
  buyer_creative_id = gflags.FLAGS.buyer_creative_id
  pretty_printer = pprint.PrettyPrinter()

  # Authenticate and construct service.
  service = sample_utils.initialize_service()

  try:
    # Create a new creative to submit.
    creative_body = {
        'accountId': account_id,
        'adgroupId': adgroup_id,
        'buyerCreativeId': buyer_creative_id,
        'HTMLSnippet': ('<html><body><a href="http://www.google.com">'
                        'Hi there!</a></body></html>'),
        'clickThroughUrl': ['http://www.google.com'],
        'width': 300,
        'height': 250,
        'advertiserName': 'google'
        }
    creative = service.creatives().insert(body=creative_body).execute()
    # Print the response. If the creative has been already reviewed, its status
    # and categories will be included in the response.
    pretty_printer.pprint(creative)
  except AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)
