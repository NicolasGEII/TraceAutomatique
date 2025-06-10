import automatique

def main() -> None:
    funct = [[1], [0,1,1]] # [[1], [0*P^2, 1*p, 1]]
    au = automatique.automatique(funct)
    au.run()

if __name__ == '__main__':
    main()
