# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:18:52 2019

@author: Utilisateur
"""
import os

def alb_collab_to_pdf(ipynb_name): 
  os.system('apt-get install texlive texlive-xetex texlive-latex-extra pandoc')
  os.system('pip install pypandoc')
  os.system('jupyter nbconvert --to PDF'+ipynb_name)
