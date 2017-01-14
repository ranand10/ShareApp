import configparser

config = configparser.ConfigParser()
config.read('share_stock_config.cfg')


def getStartTimeHours():
    return int(config.get('timings', 'start_time_hrs'))


def getStartTimeMin():
    return int(config.get('timings', 'start_time_min'))


def getStartTimeSec():
    return int(config.get('timings', 'start_time_sec'))


def getStartTimeMicSec():
    return int(config.get('timings','start_time_msec'))


def getTimeDiffHours():
    return int(config.get('timings', 'time_zone_diff_hrs'))


def getTimeDiffSec():
    return int(config.get('timings', 'time_zone_diff_sec'))


def getWaitBetweenCycle():
    return int(config.get('timings', 'max_wait_time_for_cycle_sec'))


def getBeginningSleepTime():
    return int(config.get('timings', 'sleep_time_before_beginning'))


def getRunningDataPath():
    return config.get('paths', 'running_data_path')


def getSequenceFilePath() :
    return config.get('paths','sequence_file_full_path')


def getSequenceFileName() :
    return config.get('filename','sequence_file')


def getEndTimeHrs() :
    return int(config.get('timings','end_time_hrs'))


def getEndTimeMin() :
    return int(config.get('timings','end_time_min'))


def getEndTimeSec() :
    return int(config.get('timings','end_time_sec'))


def getEndTimeMicSec() :
    return int(config.get('timings','end_time_msec'))

def getShareNameFilePath() :
    return config.get('paths','stock_name_file_path')

def getShareNameFileName() :
    return config.get('filename','stock_file_name')

def getShareNameSheetName() :
    return config.get('sheetname','share_list_sheet_name')