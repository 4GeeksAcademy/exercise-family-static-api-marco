"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    

    def add_member(self, member):
        # fill this method and update the return
        if "id" not in member:
            raise Exception("ID is required for adding a member")

        member['last_name'] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        for index, member in enumerate(self._members):
            if member['id'] == id:
                del self._members[index]
                return {"done": True}
        return {"done": False}

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member['id'] == id:
                return member

        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members