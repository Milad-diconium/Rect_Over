#!/usr/bin/env bash
#
#  _____       _     _ _     _        _____                       _        _   _       _       _                 _
# |  __ \     | |   | (_)   | |      / ____|                     | |      | \ | |     | |     | |               | |
# | |__) |   _| |__ | |_ ___| |__   | (___   __ _ _ __ ___  _ __ | | ___  |  \| | ___ | |_ ___| |__   ___   ___ | | _____
# |  ___/ | | | '_ \| | / __| '_ \   \___ \ / _` | '_ ` _ \| '_ \| |/ _ \ | . ` |/ _ \| __/ _ \ '_ \ / _ \ / _ \| |/ / __|
# | |   | |_| | |_) | | \__ \ | | |  ____) | (_| | | | | | | |_) | |  __/ | |\  | (_) | ||  __/ |_) | (_) | (_) |   <\__ \
# |_|    \__,_|_.__/|_|_|___/_| |_| |_____/ \__,_|_| |_| |_| .__/|_|\___| |_| \_|\___/ \__\___|_.__/ \___/ \___/|_|\_\___/
#                                                          | |
#                                                          |_|
#
#
# Publish the sample-notebooks folder into OLP Repository, so the customers can download it and quickly start to use sample Jupyter Notebooks.
#
# Usage:
#   ./publish_sample_notebooks.sh [--options]
#   ./publish_sample_notebooks.sh -h | --help
#
# Options:
#   -h --help                  Show help information
#   -v --version <version>     Version used for release publication. MANDATORY
#   -r --resource-repo-url <repo> Resource repo URL include https://. MANDATORY
#   -u --user <user>           Artifactory user. MANDATORY
#   -p --password <password>   Artifactory password. MANDATORY
#

# All rights reserved.
set -e

_print_usage() {
  cat <<HEREDOC

 _____       _     _ _     _        _____                       _        _   _       _       _                 _
|  __ \     | |   | (_)   | |      / ____|                     | |      | \ | |     | |     | |               | |
| |__) |   _| |__ | |_ ___| |__   | (___   __ _ _ __ ___  _ __ | | ___  |  \| | ___ | |_ ___| |__   ___   ___ | | _____
|  ___/ | | | '_ \| | / __| '_ \   \___ \ / _` | '_ ` _ \| '_ \| |/ _ \ | . ` |/ _ \| __/ _ \ '_ \ / _ \ / _ \| |/ / __|
| |   | |_| | |_) | | \__ \ | | |  ____) | (_| | | | | | | |_) | |  __/ | |\  | (_) | ||  __/ |_) | (_) | (_) |   <\__ \
|_|    \__,_|_.__/|_|_|___/_| |_| |_____/ \__,_|_| |_| |_| .__/|_|\___| |_| \_|\___/ \__\___|_.__/ \___/ \___/|_|\_\___/
                                                         | |
                                                         |_|



Publish the sample-notebooks folder into OLP Repository, so the customers can download it and quickly start to use sample Jupyter Notebooks.

Usage:
  ./$(basename "${0}") [--options]
  ./$(basename "${0}") -h | --help

Options:
  -h --help                  Show help information
  -v --version <version>     Version used for release publication. MANDATORY
  -r --resource-repo-url <repo> Resource repo URL include https://. MANDATORY
  -u --user <user>           Artifactory user. MANDATORY
  -p --password <password>   Artifactory password. MANDATORY

HEREDOC
}

_require_argument() {
  local _option="${1:-}"
  local _argument="${2:-}"

  if [[ -z "${_argument}" ]]
  then
    printf "Option requires a argument: %s\\nSee ./$(basename "${0}") --help\\n" "${_option}"
    exit 1
  fi
}

_mandatory_option() {
  local _option="${1:-}"
  local _value="${2:-}"

  if [[ -z "${_value}" ]]
  then
    printf "Option %s is mandatory.\\nSee ./$(basename "${0}") --help\\n" "${_option}"
    exit 1
  fi
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            _print_usage
            shift
            exit 0
            ;;
        -v|--version)
            _require_argument "$1" "$2"
            overlap_check_version="$2"
            shift
            shift
            ;;
        -r|--repo-url)
            _require_argument "$1" "$2"
            resource_repo_url="$2"
            shift
            shift
            ;;
        -u|--user)
            _require_argument "$1" "$2"
            artifactory_user="$2"
            shift
            shift
            ;;
        -p|--password)
            _require_argument "$1" "$2"
            artifactory_password="$2"
            shift
            shift
            ;;
        *)
            ;;
    esac
done

_mandatory_option user "$artifactory_user"
_mandatory_option password "$artifactory_password"
_mandatory_option version "$overlap_check_version"
_mandatory_option "repo-url" "$resource_repo_url"

function publish_sample_notebooks(){
  rm -rf ./overlap_check_samples.zip
  mkdir overlap_check_samples
  cp -rf published_samples/* overlap_check_samples/
  zip -r ./overlap_check_samples.zip published_samples/*
  checksum=$(md5sum ./overlap_check_samples.zip  | awk '{ print $1 }')
  artifact_url=${resource_repo_url}/overlap_check/${overlap_check_version}/
  file_path=./overlap_check_samples.zip
  curl -v -f -u "${artifactory_user}:${artifactory_password}" --header "X-Checksum-MD5:${checksum}" -X PUT "${artifact_url}" -T ${file_path}
  rm -rf ./overlap_check_samples.zip
  rm -rf overlap_check_samples/
}

publish_sample_notebooks
