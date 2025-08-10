import sys, random
import pygame, pygame_menu
from pygame_menu.menu import Menu
from pygame_menu.widgets.core.selection import Selection

class NoWrapMenu(Menu):
    def _select(
        self,
        index: int,
        update_surface: int = 1,
        event: str = '',
        apply_sound: bool = True,
        **kwargs
    ) -> 'Menu':
        if 0 <= index < len(self._widgets):
            return super()._select(index, update_surface, event, apply_sound, **kwargs)
        return self

class pypod_menu(NoWrapMenu):
   
    def __init__(self, elements):
        # Inherit from THEME_BLUE
        pypod_theme = pygame_menu.themes.THEME_BLUE.copy()
        
        # Customize to our heart's content!
        pypod_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE
        pypod_theme.title_bar_font = pygame_menu.font.FONT_OPEN_SANS_LIGHT
        pypod_theme.title_font_antialias = True
        pypod_theme.title_font_color = (0, 0, 0, 255)
        pypod_theme.title_font_shadow = False
        pypod_theme.title_font_size = 16
        pypod_theme.widget_font_size = 16
        pypod_theme.widget_alignment = pygame_menu.locals.ALIGN_LEFT
        pypod_theme.widget_font_color = (0,0,0,255)
        
        # Custom selection code (simpler, not as true to the original iPod UI)
        effect = pygame_menu.widgets.HighlightSelection(border_width=0, margin_x=10, margin_y=0)
        effect.set_background_color((69, 181, 238, 255))
        pypod_theme.widget_selection_effect = effect
                
        # Custom selection code (uses draw, which requires some level of transparency)
        # pypod_theme.widget_selection_effect = HalfRowSelection(
        #     fill=(69, 181, 238, 255),
        #     border_width=0,
        #     width_factor=0.5,
        #     left_padding=0.5,
        #     margin_y=1
        # )
        pypod_theme.selection_color = (255,255,255)

        
        pypod_theme.widget_font = pygame_menu.font.FONT_OPEN_SANS_LIGHT
        
        super().__init__('pyPodPro', 320,240,theme=pypod_theme, center_content=False)
        self.wrap_around = False
        self._theme.widget_alignment = pygame_menu.locals.ALIGN_LEFT

        # Spacer
        self.add.label('', selectable=False)
        
        # Populate the menu items
        for label, destination in elements.items():
            self.add.button(label, destination)
            
# This is needed if you want an "iPod-esque" highlight style
class HalfRowSelection(Selection):
    def __init__(self, fill=(69,181,238,80), border=(0, 40, 180), border_width=0,
                 width_factor=0.5, left_padding=0, margin_y=1):
        super().__init__(margin_left=0, margin_right=0, margin_top=margin_y, margin_bottom=margin_y)
        self.fill = fill
        self.border = border
        self.border_width = border_width
        self.width_factor = width_factor
        self.left_padding = left_padding

    def draw(self, surface: pygame.Surface, widget: pygame_menu.widgets.Widget) -> None:
        menu = widget.get_menu()

        # Height = widget height + selection margins
        row_h = widget.get_height() + self.margin_top + self.margin_bottom

        # Width = fraction of the *inner* menu width (excludes menubar/scrollbars)
        row_w = int(menu.get_width(inner=True) * self.width_factor)

        # Anchor to the menu's left edge; vertical center on the widget
        menu_rect = menu.get_rect()  # no kwargs on Menu.get_rect()
        widget_rect = widget.get_rect(to_absolute_position=True)

        x = menu_rect.left + self.left_padding
        y = widget_rect.centery - row_h // 2

        rect = pygame.Rect(x, y, row_w, row_h)

        # Respect RGBA fills by using an alpha surface when needed
        if self.fill is not None:
            pygame.draw.rect(surface, self.fill, rect)
