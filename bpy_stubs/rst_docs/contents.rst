%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Blender Documentation Contents
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


Welcome, this document is an API reference for Blender 2.79b f4dc9f9d68b, built Thu 03/22/2018.

This site can be downloaded for offline use `Download the full Documentation (zipped HTML files) <blender_python_reference_2_79b_release.zip>`_

============================
Blender/Python Documentation
============================

.. toctree::
   :maxdepth: 1

   Blender/Python Quickstart: new to Blender/scripting and want to get your feet wet? <info_quickstart.rst>

   Blender/Python API Overview: a more complete explanation of Python integration <info_overview.rst>

   Blender/Python API Reference Usage: examples of how to use the API reference docs <info_api_reference.rst>

   Best Practice: Conventions to follow for writing good scripts <info_best_practice.rst>

   Tips and Tricks: Hints to help you while writing scripts for Blender <info_tips_and_tricks.rst>

   Gotcha's: some of the problems you may come up against when writing scripts <info_gotcha.rst>


===================
Application Modules
===================

.. toctree::
   :maxdepth: 1

   bpy.context

   bpy.data

   bpy.ops

   bpy.types

   bpy.utils

   bpy.utils.previews

   bpy.path

   bpy.app

   bpy.props

==================
Standalone Modules
==================

.. toctree::
   :maxdepth: 1

   mathutils

   freestyle

   bgl

   blf

   gpu

   aud

   bpy_extras

   idprop.types

   bmesh

===================
Game Engine Modules
===================

.. toctree::
   :maxdepth: 1

   bge.types.rst

   bge.logic.rst

   bge.render.rst

   bge.texture.rst

   bge.events.rst

   bge.constraints.rst

   bge.app.rst

========
API Info
========

.. toctree::
   :maxdepth: 1

   change_log.rst



.. note:: The Blender Python API has areas which are still in development.
   
   The following areas are subject to change.
      * operator behavior, names and arguments
      * mesh creation and editing functions
   
   These parts of the API are relatively stable and are unlikely to change significantly
      * data API, access to attributes of Blender data such as mesh verts, material color,
        timeline frames and scene objects
      * user interface functions for defining buttons, creation of menus, headers, panels
      * render engine integration
      * modules: bgl, mathutils & game engine.

