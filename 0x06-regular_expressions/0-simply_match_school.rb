#!/usr/bin/env ruby

exit(puts "Usage: ./0-simply_match_school.rb <string>") if ARGV.empty?

match = ARGV[0].scan(/School/)

puts match.join
