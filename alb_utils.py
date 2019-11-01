# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:18:52 2019

@author: Utilisateur
"""

def alb_collab_to_pdf(ipynb_name): 
  !apt-get install texlive texlive-xetex texlive-latex-extra pandoc
  !pip install pypandoc
  !jupyter nbconvert --to PDF "$ipynb_name"