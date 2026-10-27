import pyramid
import kettle

def main() -> None:
    pyramid.run()
    print()
    kettle.run()

if __name__ == "__main__":
    main()