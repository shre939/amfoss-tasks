def is_prime(num)
  return false if num < 2
  (2..Math.sqrt(num).to_i).each do |i|
    return false if num % i == 0
  end
  true
end

print "Enter a number: "
n = gets.chomp.to_i
primes = (2..n).select { |num| is_prime(num) }
puts "Prime numbers up to #{n} are: #{primes}"

