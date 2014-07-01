class ApiArguments():
    ALL_VIEWS = 'all_views'
    ACTION = 'action'
    USERNAME = 'username'
    USER_NAME = 'user_name'
    USERNAMES = 'usernames'
    USER_NAMES = 'user_names'
    VIEW_CONTEXT = 'view_context'
    VIEWNAME = 'viewname'
    VIEW_NAME = 'view_name'
    VIEW_NAMES = 'view_names'
    VIEWS = 'views'
    ENABLED = 'enabled'
    IS_GLOBAL = 'is_global'
    GROUP_NAME = 'group_name'
    GROUP_ID = 'group_id'
    GROUP_IDS = 'group_ids'
    AGENT_IDS = 'agent_ids'
    TAG_IDS = 'tag_ids'
    PASSWORD = 'password'
    PERMISSIONS = 'permissions'
    NAME = 'name'
    NEW_PASSWORD = 'new_password'
    DOWNLOAD_URL = 'download_url'
    NET_THROTTLE = 'net_throttle'
    CPU_THROTTLE = 'cpu_throttle'
    SERVER_QUEUE_TTL = 'server_queue_ttl'
    AGENT_QUEUE_TTL = 'agent_queue_ttl'
    DELETE_ALL_AGENTS = 'delete_all_agents'
    MOVE_AGENTS_TO_VIEW = 'move_agents_to_view'
    COUNT = 'count'
    OFFSET = 'offset'
    QUERY = 'query'
    FILTER_KEY = 'filter_key'
    FILTER_VAL = 'filter_val'
    SORT = 'sort'
    SORT_BY = 'sort_by'
    OPERATION = 'operation'
    FULL_NAME = 'full_name'
    EMAIL = 'email'
    FORCE_REMOVE = 'force_remove'


class AgentApiArguments():
    AGENT_IDS = 'agent_ids'
    AGENT_ID = 'agent_id'
    DISPLAY_NAME = 'display_name'
    PRODUCTION_LEVEL = 'production_level'
    VIEWS = 'views'
    IP = 'ip'
    MAC = 'mac'
    REBOOT = 'reboot'
    SHUTDOWN = 'shutdown'
    APPS_REFRESH = 'apps_refresh'
    TOKEN = 'token'


class TagApiArguments():
    TAG_ID = 'tag_id'
    TAG_IDS = 'tag_ids'
    TAG_NAME = 'name'
    PRODUCTION_LEVEL = 'production_level'
    VIEW_NAME = 'view_name'


class ApiValues():
    ADD = 'add'
    DELETE = 'delete'
    TOGGLE = 'toggle'
    YES = 'yes'
    NO = 'no'
