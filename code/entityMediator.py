#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.dom.minidom import Entity

from code.Const import WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.enemy import Enemy
from code.player import Player


class EntityMediator:
    
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0  # If the enemy goes out of the left side of the screen, it is destroyed
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.left <= 0:
                ent.health = 0
                
    @staticmethod
    def __verify_collision_entity(ent1 , ent2):
        valid_interaction = False
        
        ## tiro do player no inimigo ##
        if isinstance(ent1 , Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
            if ent1.rect.colliderect(ent2.rect):
                ent1.health -= ent2.health
        elif isinstance(ent1 , PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
               
        ## Tiro do inimigo no player ## 
        elif isinstance(ent1 , Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
            if ent1.rect.colliderect(ent2.rect):
                ent1.health -= ent2.health
        elif isinstance(ent1 , EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True
            
            
        if valid_interaction == True:
            if ent1.rect.colliderect(ent2.rect):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name
                
            
    
    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score
        pass
    
    
    
    
    ## Verifica colisões entre entidades e entre elas e a janela do jogo ##
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    
    ### Mata entidades com vida <= 0 ###
    ### e remove elas da lista de entidades do jogo ###
    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)  # Give score if the entity is an enemy
                entity_list.remove(ent)  # Remove the entity from the game