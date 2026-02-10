class FireFighter:
  def __init__(self):
    self.environment = {"a": " ","b": " ","c": "F","d": " ","e": "F","f": " ","g": " ","h": " ","j": "F"}
    self.path = ["a", "b", "c", "d", "e", "f", "g", "h", "j"]

  def displayEnvironment(self):
    print("Environmrnt Status:")
    print(f"a: {self.environment["a"]} | b: {self.environment["b"]} | c: {self.environment["c"]}")
    print(f"d: {self.environment["d"]} | e: {self.environment["e"]} | f: {self.environment["f"]}")
    print(f"g: {self.environment["g"]} | h: {self.environment["h"]} | j: {self.environment["j"]}")
    print()

  def action(self):
    for room in self.path:
      print(f"Robot moved to Room : {room}")

      if self.environment[room] == "F":
        print("Fire detected! Extinguishing...")
        self.environment[room] = " "

      else:
        print("No fire detected.")

      self.displayEnvironment()

    print("Final Output: All fires extingushied!")


agent = FireFighter()
agent.action()
