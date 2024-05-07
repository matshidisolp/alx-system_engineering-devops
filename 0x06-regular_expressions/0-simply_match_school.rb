#!/usr/bin/env ruby

# Check if argument exists
if ARGV.empty?
  puts "Usage: ./0-simply_match_school.rb <string>"
  exit 1
end

# Regular expression definition
regex = /School/

# Argument and reg. expression matching
match = ARGV[0].scan(regex)

# Matched string
puts match.join
