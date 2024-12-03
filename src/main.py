import webbrowser

from src.services.map import create_map


def main():
    create_map().save("tour_map.html")
    webbrowser.open("tour_map.html")


if __name__ == '__main__':
    main()
