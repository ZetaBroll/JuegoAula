#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.dom.minidom import Entity

from code.enemy import Enemy


class EntityMediator:
    
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0  # If the enemy goes out of the left side of the screen, it is destroyed
        pass
    
    
    
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)  # Remove the entity from the game