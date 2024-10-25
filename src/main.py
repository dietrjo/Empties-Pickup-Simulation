import webbrowser

from src.services.map import generate_map


def main():
    tour_map = generate_map()
    tour_map.save("tour_map.html")
    webbrowser.open("tour_map.html")


if __name__ == '__main__':
    main()
