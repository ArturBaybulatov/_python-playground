with open('out.txt', 'w') as outfile:
    for filename in ('a.txt', 'b.txt', 'c.txt'):
        with open(filename) as file:
            outfile.write(file.read() + '\n')

print('Done')


# import code; code.interact(local=dict(globals(), **locals()))
