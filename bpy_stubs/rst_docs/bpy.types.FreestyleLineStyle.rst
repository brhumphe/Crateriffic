FreestyleLineStyle(ID)
======================

.. module:: bpy.types

base classes --- :class:`bpy_struct`, :class:`ID`

.. class:: FreestyleLineStyle(ID)

   Freestyle line style, reusable by multiple line sets

   .. attribute:: active_texture

      Active texture slot being displayed

      :type: :class:`Texture`

   .. attribute:: active_texture_index

      Index of active texture slot

      :type: int in [0, 17], default 0

   .. attribute:: alpha

      Base alpha transparency, possibly modified by alpha transparency modifiers

      :type: float in [0, 1], default 0.0

   .. data:: alpha_modifiers

      List of alpha transparency modifiers

      :type: :class:`LineStyleAlphaModifiers` :class:`bpy_prop_collection` of :class:`LineStyleAlphaModifier`, (readonly)

   .. attribute:: angle_max

      Maximum 2D angle for splitting chains

      :type: float in [0, 3.14159], default 0.0

   .. attribute:: angle_min

      Minimum 2D angle for splitting chains

      :type: float in [0, 3.14159], default 0.0

   .. data:: animation_data

      Animation data for this data-block

      :type: :class:`AnimData`, (readonly)

   .. attribute:: caps

      Select the shape of both ends of strokes

      * ``BUTT`` Butt, Butt cap (flat).
      * ``ROUND`` Round, Round cap (half-circle).
      * ``SQUARE`` Square, Square cap (flat and extended).

      :type: enum in ['BUTT', 'ROUND', 'SQUARE'], default 'BUTT'

   .. attribute:: chain_count

      Chain count for the selection of first N chains

      :type: int in [0, inf], default 0

   .. attribute:: chaining

      Select the way how feature edges are jointed to form chains

      * ``PLAIN`` Plain, Plain chaining.
      * ``SKETCHY`` Sketchy, Sketchy chaining with a multiple touch.

      :type: enum in ['PLAIN', 'SKETCHY'], default 'PLAIN'

   .. attribute:: color

      Base line color, possibly modified by line color modifiers

      :type: float array of 3 items in [0, inf], default (0.0, 0.0, 0.0)

   .. data:: color_modifiers

      List of line color modifiers

      :type: :class:`LineStyleColorModifiers` :class:`bpy_prop_collection` of :class:`LineStyleColorModifier`, (readonly)

   .. attribute:: dash1

      Length of the 1st dash for dashed lines

      :type: int in [0, 65535], default 0

   .. attribute:: dash2

      Length of the 2nd dash for dashed lines

      :type: int in [0, 65535], default 0

   .. attribute:: dash3

      Length of the 3rd dash for dashed lines

      :type: int in [0, 65535], default 0

   .. attribute:: gap1

      Length of the 1st gap for dashed lines

      :type: int in [0, 65535], default 0

   .. attribute:: gap2

      Length of the 2nd gap for dashed lines

      :type: int in [0, 65535], default 0

   .. attribute:: gap3

      Length of the 3rd gap for dashed lines

      :type: int in [0, 65535], default 0

   .. data:: geometry_modifiers

      List of stroke geometry modifiers

      :type: :class:`LineStyleGeometryModifiers` :class:`bpy_prop_collection` of :class:`LineStyleGeometryModifier`, (readonly)

   .. attribute:: integration_type

      Select the way how the sort key is computed for each chain

      * ``MEAN`` Mean, The value computed for the chain is the mean of the values obtained for chain vertices.
      * ``MIN`` Min, The value computed for the chain is the minimum of the values obtained for chain vertices.
      * ``MAX`` Max, The value computed for the chain is the maximum of the values obtained for chain vertices.
      * ``FIRST`` First, The value computed for the chain is the value obtained for the first chain vertex.
      * ``LAST`` Last, The value computed for the chain is the value obtained for the last chain vertex.

      :type: enum in ['MEAN', 'MIN', 'MAX', 'FIRST', 'LAST'], default 'MEAN'

   .. attribute:: length_max

      Maximum curvilinear 2D length for the selection of chains

      :type: float in [0, 10000], default 0.0

   .. attribute:: length_min

      Minimum curvilinear 2D length for the selection of chains

      :type: float in [0, 10000], default 0.0

   .. attribute:: material_boundary

      If true, chains of feature edges are split at material boundaries

      :type: boolean, default False

   .. data:: node_tree

      Node tree for node-based shaders

      :type: :class:`NodeTree`, (readonly)

   .. attribute:: panel

      Select the property panel to be shown

      * ``STROKES`` Strokes, Show the panel for stroke construction.
      * ``COLOR`` Color, Show the panel for line color options.
      * ``ALPHA`` Alpha, Show the panel for alpha transparency options.
      * ``THICKNESS`` Thickness, Show the panel for line thickness options.
      * ``GEOMETRY`` Geometry, Show the panel for stroke geometry options.
      * ``TEXTURE`` Texture, Show the panel for stroke texture options.

      :type: enum in ['STROKES', 'COLOR', 'ALPHA', 'THICKNESS', 'GEOMETRY', 'TEXTURE'], default 'STROKES'

   .. attribute:: rounds

      Number of rounds in a sketchy multiple touch

      :type: int in [1, 1000], default 0

   .. attribute:: sort_key

      Select the sort key to determine the stacking order of chains

      * ``DISTANCE_FROM_CAMERA`` Distance from Camera, Sort by distance from camera (closer lines lie on top of further lines).
      * ``2D_LENGTH`` 2D Length, Sort by curvilinear 2D length (longer lines lie on top of shorter lines).
      * ``PROJECTED_X`` Projected X, Sort by the projected X value in the image coordinate system.
      * ``PROJECTED_Y`` Projected Y, Sort by the projected Y value in the image coordinate system.

      :type: enum in ['DISTANCE_FROM_CAMERA', '2D_LENGTH', 'PROJECTED_X', 'PROJECTED_Y'], default 'DISTANCE_FROM_CAMERA'

   .. attribute:: sort_order

      Select the sort order

      * ``DEFAULT`` Default, Default order of the sort key.
      * ``REVERSE`` Reverse, Reverse order.

      :type: enum in ['DEFAULT', 'REVERSE'], default 'DEFAULT'

   .. attribute:: split_dash1

      Length of the 1st dash for splitting

      :type: int in [0, 65535], default 0

   .. attribute:: split_dash2

      Length of the 2nd dash for splitting

      :type: int in [0, 65535], default 0

   .. attribute:: split_dash3

      Length of the 3rd dash for splitting

      :type: int in [0, 65535], default 0

   .. attribute:: split_gap1

      Length of the 1st gap for splitting

      :type: int in [0, 65535], default 0

   .. attribute:: split_gap2

      Length of the 2nd gap for splitting

      :type: int in [0, 65535], default 0

   .. attribute:: split_gap3

      Length of the 3rd gap for splitting

      :type: int in [0, 65535], default 0

   .. attribute:: split_length

      Curvilinear 2D length for chain splitting

      :type: float in [0, 10000], default 0.0

   .. data:: texture_slots

      Texture slots defining the mapping and influence of textures

      :type: :class:`LineStyleTextureSlots` :class:`bpy_prop_collection` of :class:`LineStyleTextureSlot`, (readonly)

   .. attribute:: texture_spacing

      Spacing for textures along stroke length

      :type: float in [0.01, 100], default 0.0

   .. attribute:: thickness

      Base line thickness, possibly modified by line thickness modifiers

      :type: float in [0, 10000], default 0.0

   .. data:: thickness_modifiers

      List of line thickness modifiers

      :type: :class:`LineStyleThicknessModifiers` :class:`bpy_prop_collection` of :class:`LineStyleThicknessModifier`, (readonly)

   .. attribute:: thickness_position

      Thickness position of silhouettes and border edges (applicable when plain chaining is used with the Same Object option)

      * ``CENTER`` Center, Silhouettes and border edges are centered along stroke geometry.
      * ``INSIDE`` Inside, Silhouettes and border edges are drawn inside of stroke geometry.
      * ``OUTSIDE`` Outside, Silhouettes and border edges are drawn outside of stroke geometry.
      * ``RELATIVE`` Relative, Silhouettes and border edges are shifted by a user-defined ratio.

      :type: enum in ['CENTER', 'INSIDE', 'OUTSIDE', 'RELATIVE'], default 'CENTER'

   .. attribute:: thickness_ratio

      A number between 0 (inside) and 1 (outside) specifying the relative position of stroke thickness

      :type: float in [0, 1], default 0.0

   .. attribute:: use_angle_max

      Split chains at points with angles larger than the maximum 2D angle

      :type: boolean, default False

   .. attribute:: use_angle_min

      Split chains at points with angles smaller than the minimum 2D angle

      :type: boolean, default False

   .. attribute:: use_chain_count

      Enable the selection of first N chains

      :type: boolean, default False

   .. attribute:: use_chaining

      Enable chaining of feature edges

      :type: boolean, default False

   .. attribute:: use_dashed_line

      Enable or disable dashed line

      :type: boolean, default False

   .. attribute:: use_length_max

      Enable the selection of chains by a maximum 2D length

      :type: boolean, default False

   .. attribute:: use_length_min

      Enable the selection of chains by a minimum 2D length

      :type: boolean, default False

   .. attribute:: use_nodes

      Use shader nodes for the line style

      :type: boolean, default False

   .. attribute:: use_same_object

      If true, only feature edges of the same object are joined

      :type: boolean, default False

   .. attribute:: use_sorting

      Arrange the stacking order of strokes

      :type: boolean, default False

   .. attribute:: use_split_length

      Enable chain splitting by curvilinear 2D length

      :type: boolean, default False

   .. attribute:: use_split_pattern

      Enable chain splitting by dashed line patterns

      :type: boolean, default False

   .. attribute:: use_texture

      Enable or disable textured strokes

      :type: boolean, default False

.. rubric:: Inherited Properties

.. hlist::
   :columns: 2

   * :class:`bpy_struct.id_data`
   * :class:`ID.name`
   * :class:`ID.users`
   * :class:`ID.use_fake_user`
   * :class:`ID.tag`
   * :class:`ID.is_updated`
   * :class:`ID.is_updated_data`
   * :class:`ID.is_library_indirect`
   * :class:`ID.library`
   * :class:`ID.preview`

.. rubric:: Inherited Functions

.. hlist::
   :columns: 2

   * :class:`bpy_struct.as_pointer`
   * :class:`bpy_struct.driver_add`
   * :class:`bpy_struct.driver_remove`
   * :class:`bpy_struct.get`
   * :class:`bpy_struct.is_property_hidden`
   * :class:`bpy_struct.is_property_readonly`
   * :class:`bpy_struct.is_property_set`
   * :class:`bpy_struct.items`
   * :class:`bpy_struct.keyframe_delete`
   * :class:`bpy_struct.keyframe_insert`
   * :class:`bpy_struct.keys`
   * :class:`bpy_struct.path_from_id`
   * :class:`bpy_struct.path_resolve`
   * :class:`bpy_struct.property_unset`
   * :class:`bpy_struct.type_recast`
   * :class:`bpy_struct.values`
   * :class:`ID.copy`
   * :class:`ID.user_clear`
   * :class:`ID.user_remap`
   * :class:`ID.make_local`
   * :class:`ID.user_of_id`
   * :class:`ID.animation_data_create`
   * :class:`ID.animation_data_clear`
   * :class:`ID.update_tag`

.. rubric:: References

.. hlist::
   :columns: 2

   * :mod:`bpy.context.line_style`
   * :class:`BlendData.linestyles`
   * :class:`BlendDataLineStyles.new`
   * :class:`BlendDataLineStyles.remove`
   * :class:`FreestyleLineSet.linestyle`

