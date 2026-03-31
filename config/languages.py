# config/languages.py
# Dictionary containing all UI text for localization (VI/EN)

CONTENT = {
    "vi": {
        # =========================================================
        # NAVBAR SECTION
        # =========================================================
        "navbar": {
            "home": "Trang chủ",
            "brand": "VNWander",
            "team": "Đội ngũ",
            "career": "Tuyển dụng",
            "news": "Tin tức",
            "contact": "Liên hệ"
        },

        # =========================================================
        # HERO SECTION
        # =========================================================
        "hero": {
            "eyebrow": "VNWANDER ENTERPRISE",
            "title_white": "Nâng Tầm Trải Nghiệm",
            "title_blue": "Du Lịch Việt Nam",
            "subtitle": "Giải pháp thông minh giúp lập kế hoạch nhanh chóng, quyết định tự tin và theo dõi lộ trình dễ dàng.",
            "cta": "Yêu cầu tư vấn"
        },

        # =========================================================
        # DESTINATIONS SECTION (ĐÃ CẬP NHẬT TÊN VÀ LINK ẢNH TRỰC TIẾP)
        # =========================================================
        "destinations": {
            "title": "Điểm đến yêu thích",
            "subtitle": "Hãy chọn một điểm đến du lịch nổi tiếng dưới đây để khám phá các chuyến đi độc quyền của chúng tôi với mức giá vô cùng hợp lý.",
            "regions": {
                "north": {
                    "label": "Miền Bắc",
                    "cities": [
                        {"name": "Hà Nội", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/L%C4%83ng_B%C3%A1c_-_NKS.jpg/1280px-L%C4%83ng_B%C3%A1c_-_NKS.jpg"},
                        {"name": "Sapa", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Khu_ph%E1%BB%91_m%E1%BB%9Bi_Sa_Pa.jpg/500px-Khu_ph%E1%BB%91_m%E1%BB%9Bi_Sa_Pa.jpg"},
                        {"name": "Hạ Long", "img": "https://translate.google.com/website?sl=en&tl=vi&hl=vi&client=srp&u=https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Ha_Long_Bay_in_2019.jpg/1280px-Ha_Long_Bay_in_2019.jpg"},
                        {"name": "Ninh Bình", "img": "https://mia.vn/media/uploads/blog-du-lich/doc-dao-le-hoi-trang-an-net-van-hoa-tin-nguong-cua-ninh-binh-1640505232.jpg"},
                        {"name": "Cao Bằng", "img": "https://booking.pystravel.vn/uploads/posts/avatar/1691494369.jpg"},
                        {"name": "Mộc Châu", "img": "https://phuotvivu.com/blog/wp-content/uploads/2021/06/M%E1%BB%99c-Ch%C3%A2u-%C4%91%E1%BB%93i-ch%C3%A8.jpg"},
                        {"name": "Hà Giang", "img": "https://vcdn1-dulich.vnecdn.net/2022/03/31/mapilenghagiangvnexpress-16487-2310-5584-1648718524.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=kOOQrA2oCmdoblPaNEpo1A"}
                    ]
                },
                "central": {
                    "label": "Miền Trung",
                    "cities": [
                        {"name": "Đà Nẵng", "img": "https://vcdn1-dulich.vnecdn.net/2022/06/03/cauvang-1654247842-9403-1654247849.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=Swd6JjpStebEzT6WARcoOA"},
                        {"name": "Hội An", "img": "https://lh4.googleusercontent.com/proxy/R5W1k-qyBF2POJssyt_ApkwI5T7jWWkPlrP2d4-eTdWN0ytCTrw1T1DuNZ9Jz5b0tHA0S1sp_QsN8p_9AE9VktaL2wVGMNZwiWGXxoqKnLfydPG4n6faAA1PwYjQgYFDBmvQm77aGg"},
                        {"name": "Huế", "img": "https://cdn-media.sforum.vn/storage/app/media/ctvseo_MH/hu%E1%BA%BF%20mi%E1%BB%81n%20n%C3%A0o/hue-thuoc-mien-nao-thumbnail.jpg"},
                        {"name": "Nha Trang", "img": "https://vcdn1-dulich.vnecdn.net/2022/05/09/shutterstock-280926449-6744-15-3483-9174-1652070682.jpg?w=0&h=0&q=100&dpr=2&fit=crop&s=NSSoqK15XdlPH-RaUQ1FhQ"},
                        {"name": "Đà Lạt", "img": "https://cdn3.ivivu.com/2023/10/du-lich-Da-Lat-ivivu.jpg"},
                        {"name": "Quy Nhơn", "img": "https://www.vietnamairlines.com/content/dam/legacy-site-assets/SEO-images/2025%20SEO/Thay%20Anh%20Traffic%20Tieng%20Viet/du%20lich%20quy%20nhon/bien-quy-nhon-dep-nen-tho-thu-hut-dong-dao-du-khach-va-nguoi-dia-phuong.png"},
                        {"name": "Phú Yên", "img": "https://cdn2.tuoitre.vn/471584752817336320/2024/6/4/base64-1717479667366477194000.jpeg"}
                    ]
                },
                "southwest": {
                    "label": "Tây Nam Bộ",
                    "cities": [
                        {"name": "Cần Thơ", "img": "https://baocantho.com.vn/image/fckeditor/upload/2025/20250927/images/T3a-1-BSS.webp"},
                        {"name": "Phú Quốc", "img": "https://bcp.cdnchinhphu.vn/334894974524682240/2025/6/23/phu-quoc-17506756503251936667562.jpg"},
                        {"name": "Bến Tre", "img": "https://toquoc.mediacdn.vn/2019/7/4/vuon-trai-cay-ben-tre-1-min-15622312999881421270984.jpg"},
                        {"name": "Đồng Tháp", "img": "https://images2.thanhnien.vn/528068263637045248/2025/6/21/a1-1750486668570197012920.jpg"},
                        {"name": "An Giang", "img": "https://cdn3.ivivu.com/2025/12/du-lich-an-giang-ivivu-1.png"},
                        {"name": "Cà Mau", "img": "https://datviettour.com.vn/uploads/images/tin-tuc-SEO/mien-tay/Ca-Mau/ca-mau.jpg"}
                    ]
                },
                "southeast": {
                    "label": "Đông Nam Bộ",
                    "cities": [
                        {"name": "TP. Hồ Chí Minh", "img": "https://images.unsplash.com/photo-1583417319070-4a69db38a482?q=80&w=800&auto=format&fit=crop"},
                        {"name": "Vũng Tàu", "img": "https://www.agoda.com/wp-content/uploads/2024/07/vung-tau-vietnam-featured-1244x700.jpg"},
                        {"name": "Tây Ninh", "img": "https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a3980e5929c3fb2f971e5dfe6abb83ca0669b4132aaa79278c21e5124185cb9a0777d029253902140bb92d5d6d5d69560cd88/anh-1-5654-1101.jpeg"},
                        {"name": "Bình Dương", "img": "https://file4.batdongsan.com.vn/2021/10/11/PHJN6Zw0/20211011141504-3ca0.jpg"},
                        {"name": "Đồng Nai", "img": "https://upload.wikimedia.org/wikipedia/commons/8/85/Nh%C3%A0_th%E1%BB%9D_ch%C3%ADnh_V%C4%83n_mi%E1%BA%BFu_Tr%E1%BA%A5n_Bi%C3%AAn.jpg"},
                        {"name": "Côn Đảo", "img": "https://vcdn1-dulich.vnecdn.net/2022/03/31/dulichcondao-1648708481-164870-9979-1818-1648708511.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=iWgnrUdvvBhIghPVudw1sg"}
                    ]
                }
            }
        },
        
        # =========================================================
        # ABOUT SECTION
        # =========================================================

                "about_section": {
            "why_title": "Vì sao chọn VNWander?",
            "why_subtitle": "Tự hào là đối tác chiến lược của hơn 20,000 tổ chức uy tín và hàng triệu du khách toàn cầu. Với nền tảng công nghệ tối tân và bề dày kinh nghiệm, chúng tôi tự tin là người bạn đồng hành số 1 của bạn.",
            "cards": [
                {"icon": "👥", "title": "Đội ngũ hàng đầu", "desc": "Nhân sự giàu kinh nghiệm, chuyên môn cao và tận tâm, mang đến sự tin tưởng tuyệt đối khi hợp tác."},
                {"icon": "🔒", "title": "Bảo mật tuyệt đối", "desc": "Cam kết bảo vệ thông tin qua hợp đồng NDA khắt khe. Chỉ nhân sự dự án mới có quyền tiếp cận dữ liệu."},
                {"icon": "🚀", "title": "Công nghệ tiên phong", "desc": "Liên tục cập nhật công nghệ hiện đại nhất để tối ưu hóa năng suất và mang lại giá trị vượt trội."},
                {"icon": "🎧", "title": "Hỗ trợ 24/7", "desc": "Mọi nhu cầu của bạn đều được đội ngũ chuyên gia phản hồi và giải quyết nhanh chóng bất kể ngày đêm."}
            ],
            "values_title": "Giá trị cốt lõi",
            "values_list": ["Trung thực tuyệt đối", "Hướng tới khách hàng", "Tinh thần tập thể", "Coi nhau như gia đình", "Quyết liệt hành động", "Cởi mở & Sẻ chia", "Linh hoạt thích ứng", "Luôn là số 1"],
            "ceo_title_section": "CEO của chúng tôi nói",
            "ceo_quote": "Nhận thấy thị trường du lịch trong nước chưa có một nền tảng công nghệ đủ tốt, sứ mệnh của VNWander là mang đến lợi ích tối đa cho khách hàng thông qua các giải pháp công nghệ tiên phong, đầy sáng tạo. Chúng tôi khát khao trở thành nền tảng cốt lõi tạo nên sự thịnh vượng, nâng tầm vị thế du lịch Việt Nam trên đấu trường khu vực và vươn xa đến tầm quốc tế.",
            "ceo_name": "Trần Bình Giang",
            "ceo_pos": "CEO & Founder"
        },

        # =========================================================
        # REVIEWS SECTION
        # =========================================================
        "reviews": {
            "label": "ĐÁNH GIÁ KHÁCH HÀNG",
            "title": "Những Chuyến Đi Chân Thực",
            "cta_label": "Chi tiết",
            "items": [
                {
                    "name": "Nguyễn Văn Tuấn",
                    "date": "15/03/2026",
                    "rating": 5,
                    "testimonial": "Tuyệt vời!",
                    "detailed_review": "Chuyến đi thực sự vượt quá mong đợi của tôi. Nền tảng VNWander giúp mọi bước lên lịch trình trở nên dễ dàng."
                },
                {
                    "name": "Lê Thị B",
                    "date": "14/03/2026",
                    "rating": 5,
                    "testimonial": "Rất tốt!",
                    "detailed_review": "Chuyến đi tuyệt vời! Mọi thứ đều được chuẩn bị chu đáo và đúng như mong đợi. Tôi sẽ tiếp tục sử dụng dịch vụ."
                },
                {
                    "name": "Trần Văn C",
                    "date": "10/03/2026",
                    "rating": 5,
                    "testimonial": "Rất tốt!",
                    "detailed_review": "Trải nghiệm tuyệt vời. Mọi việc diễn ra suôn sẻ. Sẽ giới thiệu cho bạn bè."
                }
            ]
        },
        "team_page": {
            "section1_title": "NHÂN LỰC TẬN TÂM",
            "section1_text": "Đội ngũ nhân sự trẻ, năng động, sở hữu năng lực chuyên môn và tinh thần trách nhiệm cao chính là nền tảng vững chắc giúp VNWander đạt được những bước tiến vượt bậc. Chúng tôi tin rằng mỗi thành viên là một mảnh ghép quý giá, góp phần xây dựng VNWander trở thành tập thể đoàn kết, luôn nỗ lực hết mình vì mục tiêu chung và vị thế dẫn đầu.",
            "section2_title": "PHÁT TRIỂN TÀI NĂNG",
            "section2_text": "Để xây dựng đội ngũ nhân tài hùng hậu, chúng tôi không ngừng học hỏi và tổ chức các buổi đào tạo chuyên môn định kỳ. Sự thấu hiểu lẫn nhau và tinh thần cầu tiến, sáng tạo không ngừng là kim chỉ nam giúp VNWander mang lại những giá trị vượt trội cho khách hàng và thị trường.",
            "section3_title": "TẦM NHÌN LÃNH ĐẠO",
            "section3_text": "Sự thành công của VNWander không thể thiếu vai trò của những người lãnh đạo nhiệt huyết. Họ là những thuyền trưởng tài ba, luôn vững tay chèo nơi đầu sóng ngọn gió để dẫn dắt con thuyền VNWander vươn xa hơn, chinh phục những đỉnh cao mới trong tương lai."
        },
        "career_page": {
            "culture_title": "Văn hóa đời sống",
            "culture_desc_new": "Tại VNWander, sứ mệnh của chúng tôi là kiến tạo những sản phẩm tiên phong, nơi mọi giới hạn đều bị xóa nhòa để nhường chỗ cho tinh thần sáng tạo bứt phá. Chúng tôi không chỉ khuyến khích bạn vượt qua những rào cản thông thường mà còn trân trọng từng ý tưởng táo bạo nhất.<br><br>Nhịp sống mỗi ngày tại đây là sự vận động không ngừng của thị trường và khát khao chinh phục những đỉnh cao mới. Thời gian tại VNWander không gói gọn trong quy định 8 tiếng khô khan; đó là hành trình của những trải nghiệm rực rỡ, nơi bạn thỏa sức sống với đam mê tuổi trẻ, học hỏi miễn phí từ các 'cao nhân' và tận hưởng những giây phút 'chill' hết mình cùng đồng đội.<br><br>Đề cao sự minh bạch và tôn trọng bản sắc cá nhân, chúng tôi tin rằng sự khác biệt chính là sức mạnh để cùng nhau phát triển. VNWander là một cộng đồng đa sắc màu, luôn sẵn sàng mở rộng vòng tay chào đón những tài năng mới gia nhập hành trình đầy cảm hứng này.",
            "join_btn": "Tham gia ngay",
            "values_title": "Giá trị cốt lõi",
            "core_values": [
                {"title": "Sáng tạo", "desc": "Không giới hạn ý tưởng", "img": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=400"},
                {"title": "Tốc độ", "desc": "Chuyển động không ngừng", "img": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=400"},
                {"title": "Minh bạch", "desc": "Trung thực trong mọi việc", "img": "https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=400"},
                {"title": "Đồng hành", "desc": "Luôn luôn đi cùng nhau", "img": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=400"},
                {"title": "Đam mê", "desc": "Sống trọn với tuổi trẻ", "img": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=400"},
                {"title": "Đổi mới", "desc": "Dẫn dắt mọi xu hướng", "img": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?q=80&w=400"},
                {"title": "Học hỏi", "desc": "Từ những cao nhân", "img": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?q=80&w=400"},
                {"title": "Khác biệt", "desc": "Tôn trọng sự đa dạng", "img": "https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=400"}
            ]
        },  
        "news_page": {
            "title_featured": "BÀI VIẾT NỔI BẬT",
            "title_latest": "TIN TỨC MỚI NHẤT",
            "read_more": "Đọc thêm",
            "featured_post": {
                "tag": "CÔNG NGHỆ",
                "date": "29 Tháng 3, 2026",
                "author": "Bởi Anh Tuấn",
                "title": "VNWander ra mắt tính năng lên lịch trình bằng AI",
                "summary": "Người dùng giờ đây có thể tạo chuyến đi cá nhân hóa chỉ trong 30 giây nhờ trí tuệ nhân tạo, khẳng định vị thế dẫn đầu công nghệ.",
                "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=1200",
                "link": "#"
            },
            "latest_news": [
                {
                    "tag": "KINH TẾ", "date": "28 Tháng 3, 2026",
                    "title": "Người Đồng Nai thu nhập bình quân gần 250 triệu đồng năm 2030",
                    "summary": "Đồng Nai đặt mục tiêu đột phá về thu nhập bình quân đầu người, khẳng định vị thế trung tâm công nghiệp phía Nam.",
                    "img": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?q=80&w=800"
                },
                {
                    "tag": "XÃ HỘI", "date": "27 Tháng 3, 2026",
                    "title": "Từ 1/4: Vợ chồng TP.HCM thu nhập dưới 50 triệu được mua nhà ở xã hội",
                    "summary": "Chính sách mới nới lỏng điều kiện giúp nhiều gia đình trẻ có cơ hội an cư lập nghiệp tại thành phố.",
                    "img": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?q=80&w=800"
                },
                {
                    "tag": "Y TẾ", "date": "26 Tháng 3, 2026",
                    "title": "Khẩn cấp chống dịch ở TP.HCM, dựng 'hàng rào' ngăn EV71",
                    "summary": "Ngành y tế triển khai các biện pháp mạnh mẽ nhằm kiểm soát và ngăn chặn biến chủng virus nguy hiểm.",
                    "img": "https://images.unsplash.com/photo-1584036561566-baf8f5f1b144?q=80&w=800"
                }
            ]
        },

        "booking": {
            "title": "Tìm chuyến bay & Đặt phòng",
            "round_trip": "Khứ hồi",
            "one_way": "Một chiều",
            "from": "Điểm khởi hành",
            "to": "Điểm đến",
            "depart_date": "Ngày đi",
            "return_date": "Ngày về",
            "passengers_class": "Số lượng vé & Hạng ghế",
            "adult": "Người lớn",
            "search_btn": "TÌM CHUYẾN ĐI"
        },

        # =========================================================
        # FOOTER SECTION
        # =========================================================
        "footer": {
            "headquarters": "Trụ sở",
            "hotline": "Hotline: 1900 ****",
            "email": "Email: hotro@vnwander.vn",
            "address": "Tầng 20, Tòa A, HUD Tower, 37 Lê Văn Lương, Quận Thanh Xuân, Hà Nội.",
            "presence_title": "Chúng tôi có mặt",
            "cities": ["Hà Nội", "Đà Nẵng", "TP Hồ Chí Minh"],
            "connect_title": "Kết nối",
            "connect_desc": "Hãy cùng chia sẻ và cập nhật thông tin với cộng đồng VNWander",
            "follow_us": "Theo dõi chúng tôi",
            "legal_title": "Điều khoản và hỗ trợ",
            "legal_links": ["Điều khoản và điều kiện", "Chính sách bảo mật", "Liên hệ"],
            "brands_title": "Thương hiệu",
            "brands": ["VNWander Partner", "Mytour", "VNWander Connect", "Dinogo"],
            "copyright": "Copyright © 2026 - CÔNG TY CỔ PHẦN VNWANDER - Đăng ký kinh doanh số 010******* - cấp lần đầu ngày 04/09/2019"
        }
    },

    "en": {
        # =========================================================
        # NAVBAR SECTION
        # =========================================================
        "navbar": {
            "home": "Home",
            "brand": "VNWander",
            "team": "Team",
            "career": "Careers",
            "news": "News",
            "contact": "Contact"
        },

        # =========================================================
        # HERO SECTION
        # =========================================================
        "hero": {
            "eyebrow": "VNWANDER ENTERPRISE",
            "title_white": "Elevate Your",
            "title_blue": "Vietnam Travel",
            "subtitle": "Smart solutions for quick planning, confident decisions, and seamless itinerary tracking.",
            "cta": "Request Consultation"
        },

        # =========================================================
        # DESTINATIONS SECTION (ĐÃ CẬP NHẬT TÊN VÀ LINK ẢNH TRỰC TIẾP)
        # =========================================================
            "destinations": {
            "title": "Favorite Destinations",
            "subtitle": "Select a popular travel destination below to explore our exclusive trips at highly reasonable prices.",
            "regions": {
                "north": {
                    "label": "North Vietnam",
                    "cities": [
                        {"name": "Hanoi", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/L%C4%83ng_B%C3%A1c_-_NKS.jpg/1280px-L%C4%83ng_B%C3%A1c_-_NKS.jpg"},
                        {"name": "Sapa", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Khu_ph%E1%BB%91_m%E1%BB%9Bi_Sa_Pa.jpg/500px-Khu_ph%E1%BB%91_m%E1%BB%9Bi_Sa_Pa.jpg"},
                        {"name": "Ha Long", "img": "https://translate.google.com/website?sl=en&tl=vi&hl=vi&client=srp&u=https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Ha_Long_Bay_in_2019.jpg/1280px-Ha_Long_Bay_in_2019.jpg"},
                        {"name": "Ninh Binh", "img": "https://mia.vn/media/uploads/blog-du-lich/doc-dao-le-hoi-trang-an-net-van-hoa-tin-nguong-cua-ninh-binh-1640505232.jpg"},
                        {"name": "Cao Bang", "img": "https://booking.pystravel.vn/uploads/posts/avatar/1691494369.jpg"},
                        {"name": "Moc Chau", "img": "https://phuotvivu.com/blog/wp-content/uploads/2021/06/M%E1%BB%99c-Ch%C3%A2u-%C4%91%E1%BB%93i-ch%C3%A8.jpg"},
                        {"name": "Ha Giang", "img": "https://vcdn1-dulich.vnecdn.net/2022/03/31/mapilenghagiangvnexpress-16487-2310-5584-1648718524.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=kOOQrA2oCmdoblPaNEpo1A"}
                    ]
                },
                "central": {
                    "label": "Central Vietnam",
                    "cities": [
                        {"name": "Da Nang", "img": "https://vcdn1-dulich.vnecdn.net/2022/06/03/cauvang-1654247842-9403-1654247849.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=Swd6JjpStebEzT6WARcoOA"},
                        {"name": "Hoi An", "img": "https://lh4.googleusercontent.com/proxy/R5W1k-qyBF2POJssyt_ApkwI5T7jWWkPlrP2d4-eTdWN0ytCTrw1T1DuNZ9Jz5b0tHA0S1sp_QsN8p_9AE9VktaL2wVGMNZwiWGXxoqKnLfydPG4n6faAA1PwYjQgYFDBmvQm77aGg"},
                        {"name": "Hue", "img": "https://cdn-media.sforum.vn/storage/app/media/ctvseo_MH/hu%E1%BA%BF%20mi%E1%BB%81n%20n%C3%A0o/hue-thuoc-mien-nao-thumbnail.jpg"},
                        {"name": "Nha Trang", "img": "https://vcdn1-dulich.vnecdn.net/2022/05/09/shutterstock-280926449-6744-15-3483-9174-1652070682.jpg?w=0&h=0&q=100&dpr=2&fit=crop&s=NSSoqK15XdlPH-RaUQ1FhQ"},
                        {"name": "Da Lat", "img": "https://cdn3.ivivu.com/2023/10/du-lich-Da-Lat-ivivu.jpg"},
                        {"name": "Quy Nhon", "img": "https://www.vietnamairlines.com/content/dam/legacy-site-assets/SEO-images/2025%20SEO/Thay%20Anh%20Traffic%20Tieng%20Viet/du%20lich%20quy%20nhon/bien-quy-nhon-dep-nen-tho-thu-hut-dong-dao-du-khach-va-nguoi-dia-phuong.png"},
                        {"name": "Phu Yen", "img": "https://cdn2.tuoitre.vn/471584752817336320/2024/6/4/base64-1717479667366477194000.jpeg"}
                    ]
                },
                "southwest": {
                    "label": "Mekong Delta",
                    "cities": [
                        {"name": "Can Tho", "img": "https://baocantho.com.vn/image/fckeditor/upload/2025/20250927/images/T3a-1-BSS.webp"},
                        {"name": "Phu Quoc", "img": "https://bcp.cdnchinhphu.vn/334894974524682240/2025/6/23/phu-quoc-17506756503251936667562.jpg"},
                        {"name": "Ben Tre", "img": "https://toquoc.mediacdn.vn/2019/7/4/vuon-trai-cay-ben-tre-1-min-15622312999881421270984.jpg"},
                        {"name": "Dong Thap", "img": "https://images2.thanhnien.vn/528068263637045248/2025/6/21/a1-1750486668570197012920.jpg"},
                        {"name": "An Giang", "img": "https://cdn3.ivivu.com/2025/12/du-lich-an-giang-ivivu-1.png"},
                        {"name": "Ca Mau", "img": "https://datviettour.com.vn/uploads/images/tin-tuc-SEO/mien-tay/Ca-Mau/ca-mau.jpg"}
                    ]
                },
                "southeast": {
                    "label": "Southeast Vietnam",
                    "cities": [
                        {"name": "Ho Chi Minh City", "img": "https://images.unsplash.com/photo-1583417319070-4a69db38a482?q=80&w=800&auto=format&fit=crop"},
                        {"name": "Vung Tau", "img": "https://www.agoda.com/wp-content/uploads/2024/07/vung-tau-vietnam-featured-1244x700.jpg"},
                        {"name": "Tay Ninh", "img": "https://cdn.tienphong.vn/images/a6bf4f60924201126af6849ca45a3980e5929c3fb2f971e5dfe6abb83ca0669b4132aaa79278c21e5124185cb9a0777d029253902140bb92d5d6d5d69560cd88/anh-1-5654-1101.jpeg"},
                        {"name": "Binh Duong", "img": "https://file4.batdongsan.com.vn/2021/10/11/PHJN6Zw0/20211011141504-3ca0.jpg"},
                        {"name": "Dong Nai", "img": "https://upload.wikimedia.org/wikipedia/commons/8/85/Nh%C3%A0_th%E1%BB%9D_ch%C3%ADnh_V%C4%83n_mi%E1%BA%BFu_Tr%E1%BA%A5n_Bi%C3%AAn.jpg"},
                        {"name": "Con Dao", "img": "https://vcdn1-dulich.vnecdn.net/2022/03/31/dulichcondao-1648708481-164870-9979-1818-1648708511.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=iWgnrUdvvBhIghPVudw1sg"}
                    ]
                }
            }
        },

        # =========================================================
        # ABOUT SECTION
        # =========================================================
                "about_section": {
            "why_title": "Why Choose VNWander?",
            "why_subtitle": "Proud to be a strategic partner of 20,000+ prestigious organizations and millions of global travelers. With advanced technology and rich experience, we are your #1 companion.",
            "cards": [
                {"icon": "👥", "title": "Top-tier Team", "desc": "Experienced, highly specialized, and dedicated personnel, ensuring absolute trust in every partnership."},
                {"icon": "🔒", "title": "Absolute Security", "                  icon": "🔒", "title": "Absolute Security", "desc": "Commitment to information protection through strict NDA contracts. Only project personnel have access to data."},
                {"icon": "🚀", "title": "Pioneering Tech", "desc": "Constantly updating the most modern technologies to optimize productivity and deliver superior value."},
                {"icon": "🎧", "title": "24/7 Support", "desc": "All your needs are quickly responded to and resolved by our professional experts, day or night."}
            ],
            "values_title": "Core Values",
            "values_list": ["Absolute Honesty", "Customer-Centric", "Team Spirit", "Treating as Family", "Decisive Action", "Openness & Sharing", "Flexible Adaptation", "Always Number 1"],
            "ceo_title_section": "What Our CEO Says",
            "ceo_quote": "Realizing that the domestic tourism market lacked a sufficiently strong technology platform, VNWander's mission is to maximize benefits for customers through pioneering and creative travel tech solutions. We aspire to be the core platform for prosperity, elevating Vietnam's tourism status regionally and internationally.",
            "ceo_name": "Binh Giang Tran",
            "ceo_pos": "CEO & Founder"
        },

        # =========================================================
        # REVIEWS SECTION
        # =========================================================
        "reviews": {
            "label": "CLIENT FEEDBACK",
            "title": "Authentic Journeys",
            "cta_label": "Detail",
            "items": [
                {
                    "name": "Nguyen Van Tuan",
                    "date": "15/03/2026",
                    "rating": 5,
                    "testimonial": "Excellent!",
                    "detailed_review": "This trip completely exceeded my expectations. The VNWander platform made every planning step effortless."
                },
                {
                    "name": "Le Thi B",
                    "date": "14/03/2026",
                    "rating": 5,
                    "testimonial": "Very good!",
                    "detailed_review": "Great trip! Everything was well-prepared and exactly as expected. I will continue to use your service."
                },
                {
                    "name": "Tran Van C",
                    "date": "10/03/2026",
                    "rating": 5,
                    "testimonial": "Very good!",
                    "detailed_review": "Great experience. Everything went smoothly. Will recommend to others."
                }
            ]
        },
        "team_page": {
            "section1_title": "DEDICATED HUMAN RESOURCES",
            "section1_text": "A young, dynamic team with high expertise and responsibility is the solid foundation for VNWander's breakthrough steps. We believe each member is a precious puzzle piece, building VNWander into a united collective, striving for common goals and a leading position.",
            "section2_title": "TALENT DEVELOPMENT",
            "section2_text": "To build a strong team, we continuously learn and organize regular professional training sessions. Mutual understanding and a progressive, creative spirit are the guidelines helping VNWander bring outstanding values to customers and the market.",
            "section3_title": "LEADERSHIP VISION",
            "section3_text": "VNWander's success is inseparable from our enthusiastic leaders. They are talented captains, always standing at the forefront to lead the VNWander ship further, conquering new heights in the future."
        },
        "career_page": {
            "culture_title": "Life & Culture",
            "culture_desc_new": "At VNWander, our mission is to create pioneering products where boundaries are erased to make room for breakthrough creativity. We don't just encourage you to overcome ordinary barriers; we cherish every bold idea.<br><br>Daily life here is a constant movement of the market and a desire to conquer new heights. Time at VNWander is not bound by dry 8-hour regulations; it's a journey of brilliant experiences where you live your youthful passion, learn for free from 'masters', and enjoy 'chill' moments with teammates.<br><br>Upholding transparency and respecting personal identity, we believe that difference is the strength to grow together. VNWander is a vibrant community, always ready to welcome new talents to join this inspiring journey.",
            "join_btn": "Join Us Now",
            "values_title": "Core Values",
            "core_values": [
                {"title": "Creativity", "desc": "Unlimited ideas", "img": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=400"},
                {"title": "Speed", "desc": "Constant movement", "img": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=400"},
                {"title": "Transparency", "desc": "Honesty in everything", "img": "https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=400"},
                {"title": "Companionship", "desc": "Always moving together", "img": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=400"},
                {"title": "Passion", "desc": "Live youth to the fullest", "img": "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=400"},
                {"title": "Innovation", "desc": "Leading trends", "img": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?q=80&w=400"},
                {"title": "Learning", "desc": "From the masters", "img": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?q=80&w=400"},
                {"title": "Difference", "desc": "Respecting diversity", "img": "https://images.unsplash.com/photo-1531482615713-2afd69097998?q=80&w=400"}
            ]
        },
        "news_page": {
            "title_featured": "FEATURED POST",
            "title_latest": "LATEST NEWS",
            "read_more": "Read more",
            "featured_post": {
                "tag": "TECH",
                "date": "March 29, 2026",
                "author": "By Anh Tuan",
                "title": "VNWander launches AI-powered travel planner",
                "summary": "Users can now create personalized trips in just 30 seconds thanks to AI, solidifying its technology leadership.",
                "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=1200",
                "link": "#"
            },
            "latest_news": [
                {
                    "tag": "ECONOMY", "date": "March 28, 2026",
                    "title": "Dong Nai average income nearly 250 million VND by 2030",
                    "summary": "Dong Nai aims for a breakthrough in per capita income, affirming its position as a Southern industrial hub.",
                    "img": "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?q=80&w=800"
                },
                {
                    "tag": "SOCIAL", "date": "March 27, 2026",
                    "title": "From April 1: HCM City couples with income under 50m can buy social housing",
                    "summary": "New policies relax conditions, giving young families the chance to settle in the city.",
                    "img": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?q=80&w=800"
                },
                {
                    "tag": "HEALTH", "date": "March 26, 2026",
                    "title": "Emergency epidemic control in HCMC to block EV71 virus",
                    "summary": "The health sector is implementing strong measures to control dangerous virus variants.",
                    "img": "https://images.unsplash.com/photo-1584036561566-baf8f5f1b144?q=80&w=800"
                }
            ]
        },

        "booking": {
            "title": "Search Flights & Hotels",
            "round_trip": "Round-trip",
            "one_way": "One-way",
            "from": "Leaving from",
            "to": "Going to",
            "depart_date": "Depart Date",
            "return_date": "Return Date",
            "passengers_class": "Passengers & Class",
            "adult": "Adult",
            "search_btn": "SEARCH TRIPS"
        },

        # =========================================================
        # FOOTER SECTION
        # =========================================================
        "footer": {
            "headquarters": "Headquarters",
            "hotline": "Hotline: 1900 ****",
            "email": "Email: support@vnwander.vn",
            "address": "20th Floor, HUD Tower, 37 Le Van Luong, Thanh Xuan Dist, Hanoi.",
            "presence_title": "Locations",
            "cities": ["Hanoi", "Da Nang", "Ho Chi Minh City"],
            "connect_title": "Connect",
            "connect_desc": "Share and update information with the VNWander community",
            "follow_us": "Follow us",
            "legal_title": "Terms & Support",
            "legal_links": ["Terms & Conditions", "Privacy Policy", "Contact"],
            "brands_title": "Brands",
            "brands": ["VNWander Partner", "Mytour", "VNWander Connect", "Dinogo"],
            "copyright": "Copyright © 2026 - VNWANDER JOINT STOCK COMPANY - Business Registration No. 010******* - Issued on Sep 04, 2019"
        }
    }
}