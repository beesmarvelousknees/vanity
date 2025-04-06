# Bitcoin Vanity Address Generator

Generates a vanity Bitcoin address in bech32 segwit format.

Examples:

- `bc1qzvs8ukd9ugcfuyuvg2cpgxtjvvk09qn0zsammy`
- `bc1qcg49knvsn0kleclkdt4tm0z2h9g7z7q7dsammy`
- `bc1q3klzv7a34rq8hggufymgxwddkxedd59mmsammy`

On a mini PC, I let this run for a few weeks at around 20% CPU usage and found 3 addresses. It randomly generates private keys, and the associated Bitcoin address, and checks whether it ends with your vanity suffix. That's it, that's all.

## How to Run

1) In `vanity.py` add your desired vanity suffix(es) to the 'vanities' list. **I recommend a vanity suffix of 5 chars or less**. See below for details.
2) In `vanity.py` adjust the input of time.sleep() to make your CPU work harder or less hard.

```python
python -m venv .env
source .env/bin/activate
pip install bitcoin
python vanity.py
```

I use htop to monitor my CPU usage. 

I also set it up so that every 1000 attempts, an 'x' is written to `count.txt`. This way we can keep track of how many attempts we have made and gauge our progress. You need to have let `vanity.py` run for 1000 attempts first so that at least one 'x' is written.

```python
python count.py
```

## Likelihood of Finding a Vanity Address

#### Random Guess with Repetition - Probability

To calculate combinations with repetition we would do $`possible\_chars^{vanity\_length}`$. A bech32 address is made by selecting from 32 possible chars, and then we choose our desired vanity length. 

- $32^{1}$ =  32
- $32^2 = 1024$
- $32^3 = 32,768$
- $32^4 = 1,048,576$
- $32^5 = 33,554,432$
- $32^6 = 1,073,741,824$
- $32^7 = 34,359,738,368$
- $32^8 = 1,099,511,627,776$
- ...
- $32^{39} = 50,216,813,883,093,446,110,686,315,385,661,331,328,818,843,555,712,276,103,168$

Where the first 3 chars are always 'bc1' and the address length is 42 chars.

Those numbers are the total number of possible strings of length $vanity\_length$. So if you exhausted the set, you would be guaranteed to find your vanity address. 

It's intuitive to imagine that we should, on average, find our vanity address before exhausting the entire set, maybe in the middle on average, and so the probability should be:

```math
(32^{vanity\_length}+1) / 2
```

Don't forget, we are generating random addresses, so we may generate the same address twice, or more times, before exhausing the set. It turns out then that the probability of finding our vanity address is actually:

```math
32^{vanity\_length}
```

Since we don't eliminate missed guesses, and past guesses remain in the possible next guess pool, so to speak, the probability of finding our vanity address doesn't change with successive guesses. It's always the same one-in-whatever odds.

#### Guessing While Avoiding Repetition - Probability

First let's remind ourselves that we are randomly generating 256 bit private keys. From each of these we generate a corresponding bech32 address. It will be the case that various private keys produce the same address suffix that is not our target suffix. Unfortunately there's nothing we can do to avoid those repeat guesses. The only thing that we control, the random private key selection, is already guaranteed to never produce the same key twice because the key space is massive. What addresses these produce are unknown until we try it. Point being, when you randomly generate an address, and the suffix space is small enough that suffix collisions are possible, there's nothing you can do to prevent suffix collisions, you can only continue making random guesses.







