defmodule Prime do
  def is_prime(num) when num < 2, do: false
  def is_prime(num) when num == 2, do: true
  def is_prime(num) do
    Enum.all?(2..trunc(:math.sqrt(num)), fn i -> rem(num, i) != 0 end)
  end
end

IO.puts("Enter a number: ")
n = String.to_integer(IO.gets(""))

primes = Enum.filter(2..n, &Prime.is_prime/1)
IO.puts("Prime numbers up to #{n} are: #{inspect primes}")

