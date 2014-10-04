from vFense.core.status_codes import GenericCodes, GenericFailureCodes

class NotificationCodes(GenericCodes):
    NotificationCreated = 8000
    NotificationUpdated = 8001
    NotificationDeleted = 8002
    NotificationDataValidated = 8003

class NotificationFailureCodes(GenericFailureCodes):
    FailedToCreateNotification = 8100
    FailedToUpdateNotification = 8101
    FailedToDeleteNotification = 8102
    InvalidNotificationType = 8103
    InvalidNotificationPlugin = 8104
    InvalidNotificationThreshold = 8105


class EmailCodes(GenericCodes):
    EmailSettingsCreated = 11000
    EmailSettingsUpdated = 11001
    EmailSettingsDeleted = 11002


class EmailFailureCodes(GenericCodes):
    FailedToCreateEmailSettings = 8100
    FailedToUpdateEmailSettings = 8101
    FailedToDeleteEmailSettings = 8102
