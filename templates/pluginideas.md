Plugin Ideas
Plugin Ideas
# CraftLimits
limits how many times you can craft an item.
  - config.yml:
    ```yml
    {rule_name}:
        rule_friendly_name: ""
        recipe: ""
        limit: 0
    ```
    - `rule_name`: The name for the rule.  Used internally to identify the rule.
    - `rule_friendly_name`: OPTIONAL.  Replaces the `rule_name` in menus.  Supports MiniMessage formatting
    - `recipe`: The recipe to monitor.  It is not the name of the result, it is the recipe key.  This allows support for plugins and datapacks that define extra recipes.  If the recipe uses the "minecraft:" namespace, it may be omitted.
    - `limit`: The number of times the item can be crafted.  Set to a number less than 1 to disable the recipe.  
    - Example:
      ```yml
      mace_limit:
          # Defaults to "minecraft:" namespace
          recipe: "mace"
          limit: 1
      spear_limit:
          # Still works with the "minecraft:" namespace in use
          recipe: "minecraft:netherite_spear"
          limit: 4;
      no_aug_ender:
          # Identifies recipes created by datapacks or other plugins.  You still need to know the key the plugin makes the recipe with though.
          recipe: "infuse:aug_ender"
          limit: 3
      ```
