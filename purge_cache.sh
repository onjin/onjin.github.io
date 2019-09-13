#!/bin/bash

# If a command fails then the deploy stops
set -e

printf "\033[0;32mPurging cache ...\033[0m\n"
# Cloudflare purge cache
source .env
curl -X POST "https://api.cloudflare.com/client/v4/zones/${CF_ZONE}/purge_cache" \
     -H "Authorization: Bearer ${CF_KEY}" \
     -H "Content-Type: application/json" \
     --data '{"purge_everything":true}'
