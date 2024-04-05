class HelloWorld:
    def __init__(self):
        self.output = "Hello World!"

    def print_output(self):
        print(self.output)

    def main(self):
        for i in range(10):
            self.print_output()


if __name__ == "__main__":
    hello_world = HelloWorld()
    hello_world.main()
