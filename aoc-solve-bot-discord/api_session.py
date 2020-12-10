import config
from requests import Session


class API_Session(Session):
    api_endpoint: str

    def __init__(self):
        super().__init__()
        self.headers.update({
            "Cookie": f"session={config.api_token}",
            "Accept": "application/json"
        })
        self.api_endpoint = config.api_endpoint

    def get(self, **kwargs):
        return super().get(self.api_endpoint, **kwargs)

    def test_data(self):
        return {
            "event": "2020",
            "members": {
                "198552": {
                    "last_star_ts": "1607577707",
                    "id": "198552",
                    "stars": 20,
                    "completion_day_level": {
                        "9": {
                            "2": {
                                "get_star_ts": "1607491804"
                            },
                            "1": {
                                "get_star_ts": "1607490857"
                            }
                        },
                        "6": {
                            "1": {
                                "get_star_ts": "1607231126"
                            },
                            "2": {
                                "get_star_ts": "1607231243"
                            }
                        },
                        "4": {
                            "2": {
                                "get_star_ts": "1607061819"
                            },
                            "1": {
                                "get_star_ts": "1607059417"
                            }
                        },
                        "10": {
                            "1": {
                                "get_star_ts": "1607576646"
                            },
                            "2": {
                                "get_star_ts": "1607577707"
                            }
                        },
                        "3": {
                            "2": {
                                "get_star_ts": "1606973725"
                            },
                            "1": {
                                "get_star_ts": "1606971827"
                            }
                        },
                        "7": {
                            "2": {
                                "get_star_ts": "1607318498"
                            },
                            "1": {
                                "get_star_ts": "1607318041"
                            }
                        },
                        "2": {
                            "1": {
                                "get_star_ts": "1606885821"
                            },
                            "2": {
                                "get_star_ts": "1606886013"
                            }
                        },
                        "1": {
                            "1": {
                                "get_star_ts": "1606799224"
                            },
                            "2": {
                                "get_star_ts": "1606799263"
                            }
                        },
                        "8": {
                            "2": {
                                "get_star_ts": "1607404390"
                            },
                            "1": {
                                "get_star_ts": "1607404038"
                            }
                        },
                        "5": {
                            "1": {
                                "get_star_ts": "1607144977"
                            },
                            "2": {
                                "get_star_ts": "1607145098"
                            }
                        }
                    },
                    "local_score": 280,
                    "global_score": 0,
                    "name": "Joseph H"
                },
                "373020": {
                    "name": "Jordan Bertasso",
                    "last_star_ts": "1607578776",
                    "id": "373020",
                    "completion_day_level": {
                        "3": {
                            "2": {
                                "get_star_ts": "1606973583"
                            },
                            "1": {
                                "get_star_ts": "1606973325"
                            }
                        },
                        "10": {
                            "2": {
                                "get_star_ts": "1607578776"
                            },
                            "1": {
                                "get_star_ts": "1607577028"
                            }
                        },
                        "4": {
                            "1": {
                                "get_star_ts": "1607058743"
                            },
                            "2": {
                                "get_star_ts": "1607061149"
                            }
                        },
                        "6": {
                            "2": {
                                "get_star_ts": "1607254844"
                            },
                            "1": {
                                "get_star_ts": "1607254467"
                            }
                        },
                        "9": {
                            "2": {
                                "get_star_ts": "1607490934"
                            },
                            "1": {
                                "get_star_ts": "1607490429"
                            }
                        },
                        "5": {
                            "1": {
                                "get_star_ts": "1607145524"
                            },
                            "2": {
                                "get_star_ts": "1607145943"
                            }
                        },
                        "1": {
                            "1": {
                                "get_star_ts": "1606800250"
                            },
                            "2": {
                                "get_star_ts": "1606800395"
                            }
                        },
                        "8": {
                            "1": {
                                "get_star_ts": "1607404299"
                            },
                            "2": {
                                "get_star_ts": "1607405727"
                            }
                        },
                        "2": {
                            "1": {
                                "get_star_ts": "1606886073"
                            },
                            "2": {
                                "get_star_ts": "1606886455"
                            }
                        },
                        "7": {
                            "1": {
                                "get_star_ts": "1607319192"
                            },
                            "2": {
                                "get_star_ts": "1607319471"
                            }
                        }
                    },
                    "stars": 20,
                    "global_score": 0,
                    "local_score": 244
                },
                "973525": {
                    "name": "SynMQU",
                    "stars": 4,
                    "completion_day_level": {
                        "2": {
                            "2": {
                                "get_star_ts": "1607044182"
                            },
                            "1": {
                                "get_star_ts": "1607043488"
                            }
                        },
                        "1": {
                            "1": {
                                "get_star_ts": "1607031632"
                            },
                            "2": {
                                "get_star_ts": "1607036912"
                            }
                        }
                    },
                    "local_score": 8,
                    "global_score": 0,
                    "last_star_ts": "1607044182",
                    "id": "973525"
                },
                "642563": {
                    "name": "Solopie",
                    "completion_day_level": {
                        "7": {
                            "1": {
                                "get_star_ts": "1607503483"
                            },
                            "2": {
                                "get_star_ts": "1607592574"
                            }
                        },
                        "2": {
                            "1": {
                                "get_star_ts": "1607069419"
                            },
                            "2": {
                                "get_star_ts": "1607069810"
                            }
                        },
                        "6": {
                            "2": {
                                "get_star_ts": "1607499301"
                            },
                            "1": {
                                "get_star_ts": "1607497768"
                            }
                        },
                        "1": {
                            "2": {
                                "get_star_ts": "1607068555"
                            },
                            "1": {
                                "get_star_ts": "1607068055"
                            }
                        },
                        "4": {
                            "1": {
                                "get_star_ts": "1607391477"
                            },
                            "2": {
                                "get_star_ts": "1607474394"
                            }
                        },
                        "3": {
                            "1": {
                                "get_star_ts": "1607070621"
                            },
                            "2": {
                                "get_star_ts": "1607386110"
                            }
                        },
                        "5": {
                            "2": {
                                "get_star_ts": "1607496949"
                            },
                            "1": {
                                "get_star_ts": "1607496244"
                            }
                        }
                    },
                    "global_score": 0,
                    "stars": 14,
                    "local_score": 79,
                    "id": "642563",
                    "last_star_ts": "1607592574"
                },
                "642762": {
                    "completion_day_level": {
                        "10": {
                            "1": {
                                "get_star_ts": "1607599650"
                            }
                        },
                        "3": {
                            "2": {
                                "get_star_ts": "1606983511"
                            },
                            "1": {
                                "get_star_ts": "1606982649"
                            }
                        },
                        "6": {
                            "1": {
                                "get_star_ts": "1607231518"
                            },
                            "2": {
                                "get_star_ts": "1607232143"
                            }
                        },
                        "4": {
                            "1": {
                                "get_star_ts": "1607217253"
                            },
                            "2": {
                                "get_star_ts": "1607220925"
                            }
                        },
                        "9": {
                            "2": {
                                "get_star_ts": "1607508504"
                            },
                            "1": {
                                "get_star_ts": "1607507429"
                            }
                        },
                        "5": {
                            "2": {
                                "get_star_ts": "1607222779"
                            },
                            "1": {
                                "get_star_ts": "1607221957"
                            }
                        },
                        "8": {
                            "2": {
                                "get_star_ts": "1607421548"
                            },
                            "1": {
                                "get_star_ts": "1607419726"
                            }
                        },
                        "1": {
                            "2": {
                                "get_star_ts": "1606809059"
                            },
                            "1": {
                                "get_star_ts": "1606808958"
                            }
                        },
                        "7": {
                            "2": {
                                "get_star_ts": "1607343530"
                            },
                            "1": {
                                "get_star_ts": "1607339879"
                            }
                        },
                        "2": {
                            "2": {
                                "get_star_ts": "1606910335"
                            },
                            "1": {
                                "get_star_ts": "1606909786"
                            }
                        }
                    },
                    "local_score": 165,
                    "stars": 19,
                    "global_score": 0,
                    "last_star_ts": "1607599650",
                    "id": "642762",
                    "name": "snc-89"
                },
                "968789": {
                    "name": "Nataly Falero",
                    "completion_day_level": {
                        "2": {
                            "1": {
                                "get_star_ts": "1606903600"
                            },
                            "2": {
                                "get_star_ts": "1606903790"
                            }
                        },
                        "1": {
                            "2": {
                                "get_star_ts": "1606822731"
                            },
                            "1": {
                                "get_star_ts": "1606820699"
                            }
                        },
                        "6": {
                            "2": {
                                "get_star_ts": "1607249262"
                            },
                            "1": {
                                "get_star_ts": "1607248239"
                            }
                        },
                        "4": {
                            "1": {
                                "get_star_ts": "1607059946"
                            },
                            "2": {
                                "get_star_ts": "1607066424"
                            }
                        },
                        "3": {
                            "2": {
                                "get_star_ts": "1607000440"
                            },
                            "1": {
                                "get_star_ts": "1606998528"
                            }
                        },
                        "5": {
                            "1": {
                                "get_star_ts": "1607153320"
                            },
                            "2": {
                                "get_star_ts": "1607153453"
                            }
                        }
                    },
                    "global_score": 0,
                    "stars": 12,
                    "local_score": 93,
                    "last_star_ts": "1607249262",
                    "id": "968789"
                },
                "637889": {
                    "completion_day_level": {
                        "5": {
                            "2": {
                                "get_star_ts": "1607146804"
                            },
                            "1": {
                                "get_star_ts": "1607145708"
                            }
                        },
                        "3": {
                            "2": {
                                "get_star_ts": "1607054391"
                            },
                            "1": {
                                "get_star_ts": "1607053631"
                            }
                        },
                        "1": {
                            "1": {
                                "get_star_ts": "1606799556"
                            },
                            "2": {
                                "get_star_ts": "1606799616"
                            }
                        },
                        "6": {
                            "1": {
                                "get_star_ts": "1607234267"
                            },
                            "2": {
                                "get_star_ts": "1607234750"
                            }
                        },
                        "8": {
                            "1": {
                                "get_star_ts": "1607430832"
                            }
                        },
                        "4": {
                            "2": {
                                "get_star_ts": "1607067066"
                            },
                            "1": {
                                "get_star_ts": "1607065117"
                            }
                        },
                        "2": {
                            "2": {
                                "get_star_ts": "1606886140"
                            },
                            "1": {
                                "get_star_ts": "1606885691"
                            }
                        }
                    },
                    "stars": 13,
                    "global_score": 0,
                    "local_score": 123,
                    "last_star_ts": "1607430832",
                    "id": "637889",
                    "name": "Bradley Kenny"
                },
                "991425": {
                    "name": "sutantyo",
                    "stars": 4,
                    "completion_day_level": {
                        "1": {
                            "2": {
                                "get_star_ts": "1606813768"
                            },
                            "1": {
                                "get_star_ts": "1606812974"
                            }
                        },
                        "2": {
                            "2": {
                                "get_star_ts": "1606903442"
                            },
                            "1": {
                                "get_star_ts": "1606902158"
                            }
                        }
                    },
                    "global_score": 0,
                    "local_score": 18,
                    "id": "991425",
                    "last_star_ts": "1606903442"
                },
                "968949": {
                    "name": "Bailey Gibbons",
                    "id": "968949",
                    "last_star_ts": "1607497574",
                    "local_score": 185,
                    "completion_day_level": {
                        "5": {
                            "2": {
                                "get_star_ts": "1607146253"
                            },
                            "1": {
                                "get_star_ts": "1607145692"
                            }
                        },
                        "8": {
                            "2": {
                                "get_star_ts": "1607407502"
                            },
                            "1": {
                                "get_star_ts": "1607405065"
                            }
                        },
                        "1": {
                            "1": {
                                "get_star_ts": "1606804369"
                            },
                            "2": {
                                "get_star_ts": "1606804638"
                            }
                        },
                        "7": {
                            "2": {
                                "get_star_ts": "1607329815"
                            },
                            "1": {
                                "get_star_ts": "1607327650"
                            }
                        },
                        "2": {
                            "1": {
                                "get_star_ts": "1606886464"
                            },
                            "2": {
                                "get_star_ts": "1606886792"
                            }
                        },
                        "3": {
                            "2": {
                                "get_star_ts": "1606977351"
                            },
                            "1": {
                                "get_star_ts": "1606975297"
                            }
                        },
                        "6": {
                            "1": {
                                "get_star_ts": "1607237758"
                            },
                            "2": {
                                "get_star_ts": "1607238998"
                            }
                        },
                        "4": {
                            "1": {
                                "get_star_ts": "1607061230"
                            },
                            "2": {
                                "get_star_ts": "1607067914"
                            }
                        },
                        "9": {
                            "2": {
                                "get_star_ts": "1607497574"
                            },
                            "1": {
                                "get_star_ts": "1607496504"
                            }
                        }
                    },
                    "stars": 18,
                    "global_score": 0
                },
                "373076": {
                    "completion_day_level": {
                        "3": {
                            "2": {
                                "get_star_ts": "1606972362"
                            },
                            "1": {
                                "get_star_ts": "1606971829"
                            }
                        },
                        "10": {
                            "1": {
                                "get_star_ts": "1607576823"
                            },
                            "2": {
                                "get_star_ts": "1607578031"
                            }
                        },
                        "9": {
                            "1": {
                                "get_star_ts": "1607490306"
                            },
                            "2": {
                                "get_star_ts": "1607490555"
                            }
                        },
                        "4": {
                            "2": {
                                "get_star_ts": "1607059468"
                            },
                            "1": {
                                "get_star_ts": "1607058539"
                            }
                        },
                        "6": {
                            "1": {
                                "get_star_ts": "1607231136"
                            },
                            "2": {
                                "get_star_ts": "1607231469"
                            }
                        },
                        "5": {
                            "1": {
                                "get_star_ts": "1607144821"
                            },
                            "2": {
                                "get_star_ts": "1607144961"
                            }
                        },
                        "2": {
                            "2": {
                                "get_star_ts": "1606885578"
                            },
                            "1": {
                                "get_star_ts": "1606885465"
                            }
                        },
                        "7": {
                            "2": {
                                "get_star_ts": "1607318393"
                            },
                            "1": {
                                "get_star_ts": "1607318112"
                            }
                        },
                        "1": {
                            "1": {
                                "get_star_ts": "1606799228"
                            },
                            "2": {
                                "get_star_ts": "1606799334"
                            }
                        },
                        "8": {
                            "1": {
                                "get_star_ts": "1607403925"
                            },
                            "2": {
                                "get_star_ts": "1607404270"
                            }
                        }
                    },
                    "stars": 20,
                    "global_score": 0,
                    "local_score": 296,
                    "id": "373076",
                    "last_star_ts": "1607578031",
                    "name": "Thingo314"
                },
                "1020629": {
                    "name": "J5kinner",
                    "last_star_ts": "1606907685",
                    "id": "1020629",
                    "global_score": 0,
                    "completion_day_level": {
                        "2": {
                            "1": {
                                "get_star_ts": "1606907653"
                            },
                            "2": {
                                "get_star_ts": "1606907685"
                            }
                        },
                        "1": {
                            "2": {
                                "get_star_ts": "1606825381"
                            },
                            "1": {
                                "get_star_ts": "1606825258"
                            }
                        }
                    },
                    "stars": 4,
                    "local_score": 12
                },
                "991586": {
                    "name": "Emilie Hyslop",
                    "local_score": 252,
                    "completion_day_level": {
                        "5": {
                            "2": {
                                "get_star_ts": "1607148099"
                            },
                            "1": {
                                "get_star_ts": "1607147839"
                            }
                        },
                        "7": {
                            "1": {
                                "get_star_ts": "1607318710"
                            },
                            "2": {
                                "get_star_ts": "1607320195"
                            }
                        },
                        "2": {
                            "2": {
                                "get_star_ts": "1606886355"
                            },
                            "1": {
                                "get_star_ts": "1606886004"
                            }
                        },
                        "1": {
                            "1": {
                                "get_star_ts": "1606799576"
                            },
                            "2": {
                                "get_star_ts": "1606799804"
                            }
                        },
                        "8": {
                            "1": {
                                "get_star_ts": "1607404200"
                            },
                            "2": {
                                "get_star_ts": "1607406027"
                            }
                        },
                        "10": {
                            "2": {
                                "get_star_ts": "1607577867"
                            },
                            "1": {
                                "get_star_ts": "1607577027"
                            }
                        },
                        "3": {
                            "2": {
                                "get_star_ts": "1606972301"
                            },
                            "1": {
                                "get_star_ts": "1606971989"
                            }
                        },
                        "9": {
                            "1": {
                                "get_star_ts": "1607490469"
                            },
                            "2": {
                                "get_star_ts": "1607491514"
                            }
                        },
                        "6": {
                            "1": {
                                "get_star_ts": "1607231098"
                            },
                            "2": {
                                "get_star_ts": "1607231354"
                            }
                        },
                        "4": {
                            "2": {
                                "get_star_ts": "1607074987"
                            },
                            "1": {
                                "get_star_ts": "1607058946"
                            }
                        }
                    },
                    "stars": 20,
                    "global_score": 0,
                    "id": "991586",
                    "last_star_ts": "1607577867"
                },
                "1066270": {
                    "completion_day_level": {
                        "3": {
                            "2": {
                                "get_star_ts": "1606979900"
                            },
                            "1": {
                                "get_star_ts": "1606979345"
                            }
                        },
                        "2": {
                            "1": {
                                "get_star_ts": "1606904539"
                            },
                            "2": {
                                "get_star_ts": "1606905095"
                            }
                        },
                        "1": {
                            "1": {
                                "get_star_ts": "1606856012"
                            },
                            "2": {
                                "get_star_ts": "1606856097"
                            }
                        },
                        "4": {
                            "1": {
                                "get_star_ts": "1607600417"
                            }
                        }
                    },
                    "stars": 7,
                    "local_score": 39,
                    "global_score": 0,
                    "last_star_ts": "1607600417",
                    "id": "1066270",
                    "name": "Neil Roberts"
                },
                "998638": {
                    "name": "Euan Mendoza",
                    "id": "998638",
                    "last_star_ts": "1607078956",
                    "completion_day_level": {
                        "4": {
                            "1": {
                                "get_star_ts": "1607078956"
                            }
                        }
                    },
                    "global_score": 0,
                    "stars": 1,
                    "local_score": 8
                },
                "635500": {
                    "stars": 15,
                    "completion_day_level": {
                        "6": {
                            "2": {
                                "get_star_ts": "1607234639"
                            },
                            "1": {
                                "get_star_ts": "1607233592"
                            }
                        },
                        "4": {
                            "2": {
                                "get_star_ts": "1607070011"
                            },
                            "1": {
                                "get_star_ts": "1607066824"
                            }
                        },
                        "3": {
                            "1": {
                                "get_star_ts": "1606975166"
                            },
                            "2": {
                                "get_star_ts": "1606975900"
                            }
                        },
                        "1": {
                            "2": {
                                "get_star_ts": "1606799367"
                            },
                            "1": {
                                "get_star_ts": "1606799311"
                            }
                        },
                        "8": {
                            "2": {
                                "get_star_ts": "1607596160"
                            },
                            "1": {
                                "get_star_ts": "1607569948"
                            }
                        },
                        "7": {
                            "1": {
                                "get_star_ts": "1607600747"
                            }
                        },
                        "2": {
                            "1": {
                                "get_star_ts": "1606885964"
                            },
                            "2": {
                                "get_star_ts": "1606887850"
                            }
                        },
                        "5": {
                            "1": {
                                "get_star_ts": "1607146317"
                            },
                            "2": {
                                "get_star_ts": "1607146667"
                            }
                        }
                    },
                    "local_score": 141,
                    "global_score": 0,
                    "id": "635500",
                    "last_star_ts": "1607600747",
                    "name": "Sophie Kaelin"
                },
                "725267": {
                    "global_score": 0,
                    "completion_day_level": {
                        "2": {
                            "2": {
                                "get_star_ts": "1606886505"
                            },
                            "1": {
                                "get_star_ts": "1606885912"
                            }
                        },
                        "7": {
                            "2": {
                                "get_star_ts": "1607322484"
                            },
                            "1": {
                                "get_star_ts": "1607319788"
                            }
                        },
                        "1": {
                            "1": {
                                "get_star_ts": "1606799483"
                            },
                            "2": {
                                "get_star_ts": "1606799595"
                            }
                        },
                        "8": {
                            "2": {
                                "get_star_ts": "1607405615"
                            },
                            "1": {
                                "get_star_ts": "1607404601"
                            }
                        },
                        "5": {
                            "1": {
                                "get_star_ts": "1607146131"
                            },
                            "2": {
                                "get_star_ts": "1607146487"
                            }
                        },
                        "9": {
                            "2": {
                                "get_star_ts": "1607493805"
                            },
                            "1": {
                                "get_star_ts": "1607491944"
                            }
                        },
                        "4": {
                            "1": {
                                "get_star_ts": "1607059078"
                            },
                            "2": {
                                "get_star_ts": "1607060770"
                            }
                        },
                        "6": {
                            "1": {
                                "get_star_ts": "1607231546"
                            },
                            "2": {
                                "get_star_ts": "1607233941"
                            }
                        },
                        "3": {
                            "1": {
                                "get_star_ts": "1606972965"
                            },
                            "2": {
                                "get_star_ts": "1606973374"
                            }
                        },
                        "10": {
                            "1": {
                                "get_star_ts": "1607576999"
                            },
                            "2": {
                                "get_star_ts": "1607580455"
                            }
                        }
                    },
                    "stars": 20,
                    "local_score": 244,
                    "id": "725267",
                    "last_star_ts": "1607580455",
                    "name": "Matthew Roberts"
                },
                "1200723": {
                    "last_star_ts": "1607338926",
                    "id": "1200723",
                    "completion_day_level": {
                        "2": {
                            "1": {
                                "get_star_ts": "1607338328"
                            },
                            "2": {
                                "get_star_ts": "1607338926"
                            }
                        },
                        "1": {
                            "1": {
                                "get_star_ts": "1607256306"
                            },
                            "2": {
                                "get_star_ts": "1607256594"
                            }
                        }
                    },
                    "local_score": 4,
                    "stars": 4,
                    "global_score": 0,
                    "name": "Ben Talese"
                }
            },
            "owner_id": "373020"
        }


session = API_Session()
