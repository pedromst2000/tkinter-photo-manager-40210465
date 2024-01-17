from windows.Explore.exploreWindow import exploreWindow
from windows.Profile.profileWindow import profileWindow
from windows.Notifications.notificationsWindow import notificationsWindow
from windows.Dashboard.dashboardWindow import dashboardWindow
from windows.Manage.manageWindow import manageWindow
from windows.Settings.settingsWindow import settingsWindow

navigate = {
    "explore": exploreWindow,
    "profile": profileWindow,
    "notifications": notificationsWindow,
    "dashboard": dashboardWindow,
    "manage": manageWindow,
    "settings": settingsWindow,
}
