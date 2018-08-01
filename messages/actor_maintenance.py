"""
Messages for maintaining actors in the system and registry.

@author aevans
"""
from messages.base import BaseMessage


class ActorCleanup(BaseMessage):
    """
    Message for cleaning up the actor
    """

    def __init__(self, actor_address, target, sender):
        """
        Constructor

        :param actor_address:  The actor address
        :type actor_address:  ActorAddress
        :param target:  The target address
        :type target:  ActorAddress
        :param sender:  The sender address
        :type sender:  ActorAddress
        """
        super(ActorCleanup, self).__init__(target, sender)
        self.actor_address = actor_address


class CreateActor(BaseMessage):
    """
    Message for the creation of an actor
    """

    def __init__(self, actor_class, actor_config, parent_address, target, sender):
        """
        Constructor

        :param actor_class:  The class for the actor to be created
        :type actor_class:  object
        :param actor_config:  The actor configuration
        :type actor_config:  ActorConfig
        :param parent_address:  The address of the parent
        :type parent_address:  ActorAddreses
        :param target:  The target address
        :type target:  ActorAddress
        :param sender:  The sender address
        :type sender:  ActorAddress
        """
        super(CreateActor, self).__init__(target, sender)
        self.actor_class = actor_class
        self.actor_config = actor_config
        self.parent_address = parent_address


class RegisterActor(BaseMessage):
    """
    Message for registering an actor.
    """

    def __init__(self, actor_address, actor_status, target, sender):
        """
        Constructor

        :param actor_address:  The actor address
        :type actor_address:  ActorAddress
        :param actor_status:  The current status of the actor
        :type actor_status:  The actor status
        :param target:  The target address
        :type target:  ActorAddress
        :param sender:  The sender address
        :type sender:  ActorAddress
        """
        super(RegisterActor, self).__init__(target, sender)
        self.actor_address = actor_address
        self.actor_status = actor_status


class RemoveActor(BaseMessage):
    """
    Removes an actor without effecting the actor status
    """

    def __init__(self, actor_address, target, sender):
        """
        Constructor

        :param actor_address:  The address to remove
        :type actor_address:  ActorAddress
        :param target:  The target address
        :type target:  ActorAddress
        :param sender:  The sender address
        :type sender:  ActorAddress
        """
        super(RemoveActor, self).__init__(target, sender)
        self.actor_address = actor_address


class AddChild(BaseMessage):
    """
    Add a child to the system
    """

    def __init__(self, parent_address, child_address, target, sender):
        """
        Constructor

        :param parent_address:  The parent address
        :type parent_address:  ActorAddress
        :param child_address:  The child address
        :type child_address:  ActorAddress
        :param target:  The target address
        :type target:  ActorAddress
        :param sender:  The sender address
        :type sender:  ActorAddress
        """
        super(AddChild, self).__init__(target, sender)
        self.parent_address = parent_address
        self.child_address = child_address


class RemoveChild(BaseMessage):
    """
    Remove the child from the parent
    """

    def __init__(self, parent_address, child_address, target, sender):
        """
        Constructor

        :param parent_address:  The parent address
        :type parent_address:  ActorAddress
        :param child_address:  The child address
        :type child_address:  ActorAddress
        :param target:  The target address
        :type target:  ActorAddress
        :param sender:  The sender address
        :type sender:  ActorAddress
        """
        super(RemoveChild, self).__init__(target, sender)
        self.parent_address = parent_address
        self.child_address = child_address


class SetActorStatus(BaseMessage):
    """
    Set an actor status
    """

    def __init__(self, actor_address, status, target, sender):
        """
        Constructor

        :param actor_address:  The actor address.
        :type actor_address:  ActorAddress
        :param status:  The status to set
        :type status:  int
        :param target:  The target address
        :type target:  ActorAddress
        :param sender:  The sender address
        :type sender:  ActorAddress
        """
        super(SetActorStatus, self).__init__(target, sender)
        self.actor_address = actor_address
        self.status = status


class StopActor(BaseMessage):
    """
    Stop an actor
    """

    def __init__(self, target, sender):
        """
        Constructor

        :param target:  The target for the message
        :type target:  ActorAddress
        :param sender:  The message sender
        :type sender:  ActorAddress
        """
        super(StopActor, self).__init__(target, sender)