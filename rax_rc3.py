#!/usr/bin/python

import json
import os
import sys
import shlex







def main():
  module = AnsibleModule(
    argument_spec = dict(
      command     = dict(default='list_cloudnets', choices=['list_cloudnets', 'get_cloudnet', 'get_lb_pools', 'get_lb_pool', 'get_lb_pool_nodes', 'add_lb_pool_node', 'get_lb_pool_nodes_details', 'get_lb_pool_node', 'remove_lb_pool_node', 'get_lb_pool_node_detail']),
      tenant_id   = dict(required=True),
      lb_id       = dict(required=False),
      lb_pool_id  = dict(required=False),
      server_id   = dict(required=False)
    ),
    supports_check_mode=False
  )
    







from ansible.module_utils.basic import *
main()
