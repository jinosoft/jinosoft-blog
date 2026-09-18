+++
date = '{{ .Date }}'
draft = true
slug = '{{ .File.ContentBaseName }}'
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
description = ''
tags = []
categories = ['IT개발']
+++
