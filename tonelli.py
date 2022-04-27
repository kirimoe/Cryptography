from sage.rings.finite_rings.integer_mod import square_root_mod_prime_power

a=Mod(4,7)
print(a)
b=square_root_mod_prime_power(a,2,20)
b^2 == a

print(a,b)