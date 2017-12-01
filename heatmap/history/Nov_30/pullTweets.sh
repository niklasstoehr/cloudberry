#!/usr/bin/env bash
cat <<EOF | curl -XPOST -d @- localhost > data.json
for \$t in dataset twitter.ds_tweet
    where ftcontains(\$t.text, ['zika','ZIKA'], {"mode":"any"})
    and \$t.create_at >= datetime("2016-06-01T00:00:00.000Z")
    and \$t.create_at < datetime("2016-12-31T00:00:00.000Z")
    return \$t
EOF
