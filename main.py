import automatique

def main() -> None:
    funct = [[1], [0,1,1]] # [[n], [P^n]]
    au = automatique.automatique(funct)
    au.run()

if __name__ == '__main__':
    main()