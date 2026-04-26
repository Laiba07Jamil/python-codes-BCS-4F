graph = {'S' : [('A,3' ), ('B,6'),('C,5')],
         'A' : [('D',9),('E',8)],
         'B':[('F',12),('G',14)],
         'C' :[('H',7)],
         'H':[('I',5),('J',6)],
         'I':[('K',1),('L',10),('M',2)],
         'D':[],
         'E':[],
         'F':[],
         'G':[],
         'J':[],
         'K':[],
         'L':[],
         'M':[]}

def beam_search(start,goal,beam_width ):
    beam = [(0,[start])]

    while beam:
        candiadte = []

        for path ,cost in beam:
            current_node = path[-1]
            if current_node == goal:
                return path,cost
            
            for neighbour , egde_cost in graph.get(current_node,[]):
                new_cost = cost + egde_cost
                new_path = path + [neighbour]
                candiadte.append(new_cost,new_path)
                candiadte.sort(key=lambda x: x[0])

    return None,float('inf')

start = 'S'
goal = 'L'
beam_width = 2
path ,cost = beam_search(start,goal,beam_width)