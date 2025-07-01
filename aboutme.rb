#!/usr/bin/env ruby

class User
  def initialize(name, pronouns, language)
    @name = name
    @pronouns = pronouns
    @language = language
  end

  def say_hi
    puts "Hello! I'm #{@name}, and welcome to my readme!"
  end
end

if __FILE__ == $0
  ghostyx = User.new('Ghostyx', 'he/him', 'English')
  ghostyx.say_hi
end
