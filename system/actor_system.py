"""
The actor registry.

@author aevans
"""
from multiprocessing import Queue

from actors.networked_actor import NetworkedActor
from messages.system_maintenance import SetConventionLeader, RegisterRemoteSystem, UnRegisterRemoteSystem
from networking.socket_server import SocketServerSecurity


class ActorSystem(NetworkedActor):

    def __init__(self,
                 actor_config,
                 system_address,
                 host,
                 port,
                 parent=[],
                 max_threads=1000,
                 signal_queue=Queue(),
                 message_queue=Queue(),
                 security=SocketServerSecurity()):
        self.is_convention_leader = False
        self.convention_leader = None
        self.__remote_systems = {}
        super(NetworkedActor, self).__init(
                self,
                actor_config,
                system_address,
                host,
                port,
                parent,
                max_threads,
                signal_queue,
                message_queue,
                security)

    def __handle_set_convention_leader(self, message, sender):
        """
        Handle setting of a convention leader.

        :param message:  The message to handle
        :type message:  BaseMessage
        :param sender:  The message sender
        :type sender:  ActorAddress
        """
        self.convention_leader = message.actor_address
        my_addr = self.config.myAddress
        if my_addr.host is message.host and my_addr.port is message.port:
            self.is_convention_leader = True

    def __handle_register_remote_system(self, message, sender):
        """
       Handle setting of a convention leader.

       :param message:  The message to handle
       :type message:  BaseMessage
       :param sender:  The message sender
       :type sender:  ActorAddress
       """
        system_addr = message.system_address.__repr__()
        self.__remote_systems[system_addr] = message.system_address

    def __handle_unregister_remote_system(self, message, sender):
        """
       Handle setting of a convention leader.

       :param message:  The message to handle
       :type message:  BaseMessage
       :param sender:  The message sender
       :type sender:  ActorAddress
       """
        system_addr = message.system_address.__repr__()
        if self.__remote_systems.get(system_addr, None):
            self.__remote_systems.pop(system_addr)

    def receive(self, message, sender):
        """
        Handle the receipt of a message to the actor system.

        :param message:  The message to handle
        :type message:  BaseMessage
        :param sender:  The message sender
        :type sender:  ActorAddress
        """
        if type(message) is SetConventionLeader:
            self.__handle_set_convention_leader(message, sender)
        elif type(message) is RegisterRemoteSystem:
            self.__handle_register_remote_system(message, sender)
        elif type(message) is UnRegisterRemoteSystem:
            self.__handle_unregister_remote_system(message, sender)
        else:
            err_msg = 'Message Handle Not Implemented {} @ {}'.format(
                str(type(message)),
                self.config.myAddress
            )
            raise NotImplemented(err_msg)
