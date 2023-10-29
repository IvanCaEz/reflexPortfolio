"""Welcome to Reflex!."""

from ReflexPortfolio import styles

# Import all the pages.
from ReflexPortfolio.pages import *

import reflex as rx

class Header:
    def __init__(self) -> None:
        self.header = rx.hstack(style = styles.header_style)

        self.crumbs = rx.breadcrumb()
        crumb_list = [
            ["/gmail_icon.png", "ivanmartinezca10@gmail.com", "mailto:ivanmartinezca10@gmail.com"],
            ["/github_icon.png", "Github", "https://github.com/IvanCaEz"]
        ]
        self.crumbs.children = [self.create_breadcrumb_item(path, title, url) for path, title, url in crumb_list]
        self.theme = rx.color_mode_button(
            rx.color_mode_icon(),
            color_scheme="gray",
            _light={"color": "black"},
            _dark = {"color": "white"}
        )
        
    def create_breadcrumb_item(self, path: str, title: str, url: str) -> rx.Component:
        if "gmail" in path:
            return  rx.breadcrumb_item(
                rx.hstack(
                    rx.image(src=path, html_width="24px", html_height="24px"),
                    rx.breadcrumb_link(title, href=url, _dark={"color": "rgba(255,255,255,0.7)"})
                )
            )
        else:
            return rx.breadcrumb_item(
                rx.hstack(
                    rx.image(src=path, html_width="24px", html_height="24px",
                             _dark={"filter": "brightness(0) invert(1)"}),
                    rx.breadcrumb_link(title, href=url, _dark={"color": "rgba(255,255,255,0.7)"})
                )
            )
        
    def compile_component(self) -> list[rx.Hstack]:
        return [self.crumbs, rx.spacer(), self.theme]

    
    def build(self) -> rx.Hstack:
        self.header.children = self.compile_component()
        return self.header
    
    
class Main:
    def __init__(self) -> None:
        self.box = rx.box(width = "100%")
        self.name = rx.hstack(
            rx.heading(
                "Hi! I'm Ivan Martinez",
                font_size=["2rem", "2.85rem", "4rem", "5rem", "5rem"],
                font_weight="900",
                _dark = {"background": "linear-gradient(to right, #e1e1e1, #757575)",
                         "background_clip": "text"
                         }
                ),
            rx.heading("👋🏻", size =  "2xl", style = styles.animation_wave),
            spacing = "1.75rem"   
            )
        self.badge_stack_max = rx.hstack(spacing = "1rem")
        self.badge_stack_min = rx.hstack(spacing = "1.25rem")
        titles = ["Software Engineer", "Backend Developer"]
        self.badge_stack_max.children = [self.create_badges(title) for title in titles]
        self.badge_stack_min.children = [self.create_badges(title) for title in titles]
        
        
    def create_badges(self, title: str) -> rx.Component:
        return rx.badge(
            title,
            variant="solid",
            padding=["0.15em 0.35em",
                     "0.15em 0.35em",
                     "0.15em 1em",
                     "0.15em 1em",
                     "0.15em 1em"],)
        
    
    def compile_desktop_component(self):
        return rx.tablet_and_desktop(
            rx.vstack(
                self.name,
                self.badge_stack_max,
                style = styles.main_style
            )
        )
        
    def compile_mobile_component(self):
        return rx.mobile_only(
            rx.vstack(
                self.name,
                self.badge_stack_min,
                style = styles.main_style
            )
        )
        
    def build(self) -> rx.Box:
        self.box.children = [self.compile_desktop_component()]
        return self.box
        
class Footer:
    def __init__(self) -> None:
        self.footer = rx.hstack(style = styles.footer_style)
        self.footer.children.append(
            rx.text("© 2023 Ivan Martinez", font_size = "10px", font_weight="bold")
        )
    
    def build(self):
        return self.footer

@rx.page("/", "Landing page")
def landing() -> rx.Component:
    header: object = Header().build()
    main: object = Main().build()
    footer: object = Footer().build()
    return rx.vstack(
        header,
        main,
        footer,
        # Background 
        _light = {
        "background" : "radial-gradient(circle, rgba(255,255,255,0.35) 1px transparent 1px)",
        "background_size" : "200px 200px"
        },
        background = "radial-gradient(circle, rgba(255,255,255,0.09) 1px transparent 1px)",
        background_size = "200px 200px",
        style = styles.animation_dots
    )
app = rx.App(style = styles.app_general_style)
app.compile()
