from vFense.plugins.patching.status_codes import PackageCodes
class CommonAppKeys():
    ViewName = 'view_name'
    Id = 'id'
    APP_ID = 'app_id'
    APP_NAME = 'app_name'
    APP_VERSION = 'app_version'
    APP_URIS = 'app_uris'
    AGENTID = 'agent_id'
    COUNT = 'count'
    AGENT_COUNT = 'agent_count'
    AGENTS = 'agents'
    STATUS = 'status'
    NAME = 'name'
    VERSION = 'version'
    INSTALLED = 'installed'
    AVAILABLE = 'available'
    PENDING = 'pending'
    SOFTWAREINVENTORY = 'Software Inventory'
    OS = 'OS'
    CUSTOM = 'Custom'
    SUPPORTED = 'Supported'
    AGENT_UPDATES = 'Agent Updates'
    ValidPackageStatuses = (INSTALLED, AVAILABLE, PENDING)
    YES = 'yes'
    NO = 'no'
    ValidHiddenVals = (YES, NO)
    UPDATES = 'Updates'
    BASIC_RV_STATS = 'basic_rv_stats'
    APP_STATS = 'app_stats'
    AGENT_STATS = 'agent_stats'

class AppStatuses():
    INSTALLED = 'installed'
    AVAILABLE = 'available'
    PENDING = 'pending'

    @staticmethod
    def get_values():
        valid_statuses = (
            map(
                lambda x:
                getattr(AppStatuses, x), dir(AppStatuses)[:-3]
            )
        )
        return valid_statuses

class CommonFileKeys():
    PKG_NAME = 'file_name'
    PKG_SIZE = 'file_size'
    PKG_URI = 'file_uri'
    FILE_URIS = 'file_uris'
    PKG_HASH = 'file_hash'
    PKG_URIS = 'uris'
    PKG_FILEDATA = 'file_data'
    PKG_CLI_OPTIONS = 'cli_options'

class CommonSeverityKeys():
    CRITICAL = 'Critical'
    OPTIONAL = 'Optional'
    RECOMMENDED = 'Recommended'
    ValidRvSeverities = (CRITICAL, RECOMMENDED, OPTIONAL)

    @staticmethod
    def get_valid_severities():
        valid_values = (
            map(
                lambda x:
                getattr(CommonSeverityKeys, x), dir(CommonSeverityKeys)[:-3]
            )
        )
        return valid_values


class FileLocationUris():
    PACKAGES = 'packages'


class SharedAppKeys():
    AppId = 'app_id'
    Id = 'id'
    InstallDate = 'install_date'
    Status = 'status'
    Hidden = 'hidden'
    AgentId = 'agent_id'
    Views = 'views'
    Name = 'name'
    Hidden = 'hidden'
    Description = 'description'
    ReleaseDate = 'release_date'
    RebootRequired = 'reboot_required'
    Kb = 'kb'
    FileSize = 'file_size'
    FileData = 'file_data'
    SupportUrl = 'support_url'
    Version = 'version'
    OsCode = 'os_code'
    vFenseSeverity = 'vfense_severity'
    VendorSeverity = 'vendor_severity'
    VendorName = 'vendor_name'
    FilesDownloadStatus = 'files_download_status'
    VulnerabilityId = 'vulnerability_id'
    VulnerabilityCategories = 'vulnerability_categories'
    CveIds = 'cve_ids'
    Dependencies = 'dependencies'
    LastModifiedTime = 'last_modified_time'
    Update = 'update'

class InstallDefaults():
    @staticmethod
    def reboot():
        return 'none'

    @staticmethod
    def cpu_throttle():
        return 'normal'

    @staticmethod
    def net_throttle():
        return 0

    @staticmethod
    def operation():
        return 'install_os_apps'

    @staticmethod
    def agent_ids():
        return list()

    @staticmethod
    def app_ids():
        return list()

class AppDefaults():
    @staticmethod
    def reboot_required():
        return 'possible'

    @staticmethod
    def hidden():
        return 'no'

    @staticmethod
    def update():
        return PackageCodes.ThisIsNotAnUpdate

    @staticmethod
    def download_status():
        return PackageCodes.FileCompletedDownload

    @staticmethod
    def vfense_severity():
        return 'Optional'

    @staticmethod
    def vuln_categories():
        return list()

    @staticmethod
    def vuln_id():
        return str()

    @staticmethod
    def cve_ids():
        return list()

    @staticmethod
    def dependencies():
        return list()

    @staticmethod
    def views():
        return list()

class FileDefaults():
    @staticmethod
    def agent_ids():
        return list()

    @staticmethod
    def app_ids():
        return list()


class RebootValues():
    POSSIBLE = 'possible'
    NO = 'no'
    REQUIRED = 'required'

    @staticmethod
    def get_values():
        valid_values = (
            map(
                lambda x:
                getattr(
                    RebootValues, x),
                dir(RebootValues)[:-3]
            )
        )
        return valid_values


class HiddenValues():
    YES = 'yes'
    NO = 'no'

    @staticmethod
    def get_values():
        valid_values = (
            map(
                lambda x:
                getattr(
                    HiddenValues, x),
                dir(HiddenValues)[:-3]
            )
        )
        return valid_values

class UninstallableValues():
    YES = 'yes'
    NO = 'no'

    @staticmethod
    def get_values():
        valid_values = (
            map(
                lambda x:
                getattr(
                    UninstallableValues, x),
                dir(UninstallableValues)[:-3]
            )
        )
        return valid_values