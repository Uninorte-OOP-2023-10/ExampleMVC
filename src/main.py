from views.client import ClientView

def main() -> None:
    ClientView(
        title = 'MVC Example',
        resolution = '300x300'
    )

if __name__ == '__main__':
    main()