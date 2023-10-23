import math

# This works if your font setting in Wing is LUCINDA SANS TYPEWRITER. Other fonts
# may work but if the font characters horitzontal footprints are not all the same
# the alignment will be thrown off by the varying character width.
# @copyright Deborah Kitchin

def main():
    # simple fstring versus book demo
    print('pi={:.2f}'.format(math.pi))      # book formatting
    print(f'pi={math.pi:.2f}')              # formatting we will use - fstring

    print(f'\n===zeros===')
    for value in range(2, 11, 2):
        print(f'{value:02} {value*value:003} {value*value*value:00004}')

    print(f'\n==centered====')
    for value in range(2, 11, 2):
        print(f'{value:^10}|{value*value:^10}|{value*value*value:^10}|')

    print(f'\n=====left====')
    for value in range(2, 11, 2):
        print(f'{value:<2}|{value*value:<3}|{value*value*value:<4}|')

    print(f'\n=====right====')
    for value in range(2, 11, 2):
        print(f'{value:>2}|{value*value:>3}|{value*value*value:>4}|')

    print(f'\n=====tabs====')
    for value in range(2, 11, 2):
        print(f'{value:>2}\t{value*value:>3}\t{value*value*value:>4}')

if __name__ == "__main__":
    main()