class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # we use this below list for checking whether all list have been visited or not
        visited=[False]*len(rooms)
        # per condition room 0 is always unlocked
        visited[0]=True
        #we use stack for acquiring key to next room so as to visit that room
        # we have initialised stack with room 0
        stack=[0]
        #we then start visiting other rooms
        while stack:
            # imagine rooms as nodes of graphs and keys as edge?
            node=stack.pop()
            # we at any given time stack will contain the next room number
            for key in rooms[node]:
                # we check whether the current room was already visited or not
                if not visited[key]:
                    # we set the flag true since it was not previously visited
                    visited[key]=True
                    #we add the key to stack
                    stack.append(key)
        return all(visited)
