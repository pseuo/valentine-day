# Valentine-Day

一个用于记录情侣纪念日的静态网页。页面包含恋爱计时、照片轮播、背景音乐、雪花动画和情话展示，适合部署成个人纪念日页面或节日告白页面。

## 功能特点

- 恋爱计时：实时显示从指定日期开始经过的天、小时、分钟和秒数。
- 照片轮播：自动切换纪念照片，并展示对应文案。
- 背景音乐：支持自动播放和点击右上角按钮暂停/继续播放。
- 雪花动画：基于 `three.js` 渲染飘雪效果。
- 移动端适配：页面以手机竖屏访问为主，同时可在桌面浏览器打开。
- 分享信息：内置 Open Graph 元信息，便于分享时展示标题、描述和封面图。

## 项目结构

```text
.
├── index.html              # 页面入口，包含主要结构和交互脚本
├── css/
│   └── index.css           # 页面样式
├── js/
│   ├── count-time.js       # 恋爱计时逻辑
│   ├── jquery.js           # jQuery 依赖
│   └── three.js            # 雪花动画依赖
├── images/                 # 页面照片
│   └── snow/               # 雪花动画素材
├── media/                  # 背景音乐文件和裁剪后的音频
├── font/                   # 自定义字体
├── favicon.ico             # 网站图标
├── pic-icon.png            # 分享封面图
├── cut-music.py            # 音频裁剪辅助脚本
└── tinyimage.py            # 图片压缩辅助脚本
```

## 本地运行

这是一个纯静态项目，不需要安装前端依赖。

### 方式一：直接打开

双击 `index.html`，使用浏览器打开即可预览。

### 方式二：启动本地静态服务

如果浏览器对本地音频、字体或资源加载有限制，建议使用本地服务运行：

```bash
python -m http.server 8080
```

然后访问：

```text
http://localhost:8080
```

## 个性化配置

主要配置集中在 `index.html` 中。

### 修改纪念日起始时间

找到以下代码，将时间改成你们的纪念日：

```html
<script>
  countTime('2025/10/18 00:00', 'day', 'hour', 'minute', 'second');
</script>
```

时间建议写成 `年/月/日 小时:分钟` 的格式。

例如，如果纪念日是 2024 年 2 月 14 日晚上 8 点，可以这样写：

```js
countTime('2024/02/14 20:00', 'day', 'hour', 'minute', 'second');
```

只需要改第一个时间，后面的 `day`、`hour`、`minute`、`second` 不用改。

### 修改双方名字

找到：

```html
<p class="our-name self-design">Bai <span>&</span> Yang</p>
```

改成你想展示的名字。

### 修改照片和文案

照片列表和文案列表位于 `index.html` 底部：

```js
var imgList = ['./images/love.jpg', './images/1.jpg', './images/2.jpg', './images/3.jpg', './images/1.jpg', './images/love.jpg'];
var imgDescList = ['轻轻地说一声：“我喜欢你！”','你往前走，我一定在你身后','You are my today and all of my tomorrows.','你是我的今天和所有的明天','"love you to the moon and back" - 《Guess How Much | Love You》','轻轻地说一声：“我喜欢你！”'];
```

注意：

- `imgList` 和 `imgDescList` 建议保持数量一致。
- 新照片可以放到 `images/` 目录中，再把路径加入 `imgList`。
- 轮播间隔默认为 `3000` 毫秒，可在 `setInterval(..., 3000)` 中修改。

### 修改背景音乐

找到：

```html
<source src="./media/zui-mei-qing-lv-cut.mp3" type="audio/mpeg">
```

将 `src` 改成 `media/` 目录下其他音乐文件，或放入新的 `.mp3` 文件后引用。

### 修改页面标题和分享信息

基础页面标题在 `index.html` 的 `<head>` 中：

```html
<title>宝贝,感谢你一直的陪伴！</title>
```

分享标题、描述和封面图可修改以下 Open Graph 信息：

```html
<meta property="og:description" content="记录“我们在一起走过点点滴滴”">
<meta property="og:title" content="轻轻地说一声：“我喜欢你！”">
<meta property="og:image" content="@pic-icon.png">
```

如果部署到自己的域名，建议同步修改 `og:url` 和 `og:image` 为自己的线上地址，例如 `https://example.com/pic-icon.png`。

## 部署

该项目可以部署到任意静态托管平台，例如：

- GitHub Pages
- Netlify
- Vercel
- Cloudflare Pages
- Nginx 静态目录

部署时上传整个项目目录即可，入口文件为 `index.html`。

## 浏览器提示

现代浏览器通常会限制未交互时自动播放音乐。如果打开页面后没有声音，可以点击右上角音乐按钮手动播放。

## 音频裁剪脚本

`cut-music.py` 可以用来裁剪 MP3 音频片段。

使用前需要安装依赖：

```bash
pip install pydub
```

如果直接运行，会使用脚本里的默认配置：

```bash
python cut-music.py
```

也可以通过参数指定输入文件、输出文件和裁剪时间：

```bash
python cut-music.py -i ./media/zui-mei-qing-lv.mp3 -o ./media/zui-mei-qing-lv-cut.mp3 -s 0:08 -e 1:37
```

参数说明：

- `-i` 或 `--input`：输入音频文件路径。
- `-o` 或 `--output`：输出音频文件路径。
- `-s` 或 `--start`：开始时间，支持 `MM:SS` 或 `HH:MM:SS`。
- `-e` 或 `--end`：结束时间，支持 `MM:SS` 或 `HH:MM:SS`。

如果导出失败，请确认本机已经安装并配置好 `ffmpeg`。

## 图片压缩脚本

`tinyimage.py` 会读取 `origin_images/` 目录中的图片，压缩后输出到 `images/` 目录，并把生成的图片路径复制到剪贴板，方便粘贴到 `imgList` 中。

使用前需要安装依赖：

```bash
pip install pillow pyperclip
```

使用方式：

```bash
python tinyimage.py
```

注意：

- 请先创建 `origin_images/` 目录，并把原始图片放进去。
- 支持 `.jpg`、`.jpeg`、`.png` 和 `.webp` 图片。
- 小于约 `1.5MB` 的图片会直接处理输出，超过该大小的图片会按脚本配置压缩。

## 素材说明

项目中包含图片、字体和音频素材。公开部署前，请确认相关素材拥有使用授权，避免版权风险。
