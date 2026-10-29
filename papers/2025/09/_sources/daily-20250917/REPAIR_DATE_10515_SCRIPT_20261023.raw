document.addEventListener('DOMContentLoaded', function() {
    const currentYear = document.getElementById('current-year');
    if (currentYear) {
        currentYear.textContent = new Date().getFullYear();
    }

    setupMobileMenu();
    setupSmoothScroll();
    setupNavHighlight();
    makeAllLinksOpenInNewTab();
    setupLinkObserver();

    loadNews();
    loadHonors();
    loadPublications();
});

function setupMobileMenu() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (!mobileMenuBtn || !mobileMenu) {
        return;
    }

    mobileMenuBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });

    mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.add('hidden');
        });
    });
}

function setupSmoothScroll() {
    const navLinks = document.querySelectorAll('.nav-links a, .mobile-menu a');

    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            const href = this.getAttribute('href');
            if (!href || !href.startsWith('#')) {
                return;
            }

            const target = document.querySelector(href);
            if (!target) {
                return;
            }

            event.preventDefault();
            const nav = document.querySelector('.top-nav');
            const navHeight = nav ? nav.offsetHeight : 0;
            const top = target.offsetTop - navHeight - 20;

            window.scrollTo({
                top,
                behavior: 'smooth'
            });
        });
    });
}

function setupNavHighlight() {
    const navLinks = document.querySelectorAll('.nav-links a');
    const sections = document.querySelectorAll('section[id]');
    const nav = document.querySelector('.top-nav');

    if (!navLinks.length || !sections.length || !nav) {
        return;
    }

    window.addEventListener('scroll', () => {
        let current = '';
        const navHeight = nav.offsetHeight;

        sections.forEach(section => {
            if (window.pageYOffset >= section.offsetTop - navHeight - 100) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            const target = (link.getAttribute('href') || '').replace('#', '');
            if (target === current || (current === 'homepage' && target === 'about')) {
                link.classList.add('active');
            }
        });
    });
}

function loadNews() {
    const homeContainer = document.getElementById('news-container');
    const allContainer = document.getElementById('all-news-container');

    if (!homeContainer && !allContainer) {
        return;
    }

    fetch(getDataPath('news.json'))
        .then(handleJsonResponse)
        .then(items => {
            if (homeContainer) {
                renderNewsItems(items.slice(0, 3), homeContainer);
            }
            if (allContainer) {
                renderNewsItems(items, allContainer);
            }
        })
        .catch(error => {
            console.error('Error loading news data:', error);
        });
}

function loadHonors() {
    const homeContainer = document.getElementById('honors-container');
    const allContainer = document.getElementById('all-honors-container');

    if (!homeContainer && !allContainer) {
        return;
    }

    fetch(getDataPath('honors.json'))
        .then(handleJsonResponse)
        .then(items => {
            if (homeContainer) {
                renderHonorsItems(items.slice(0, 8), homeContainer);
            }
            if (allContainer) {
                renderHonorsItems(items, allContainer);
            }
        })
        .catch(error => {
            console.error('Error loading honors data:', error);
        });
}

function loadPublications() {
    const featuredContainer = document.getElementById('featured-publications-container');
    const preprintContainer = document.getElementById('featured-preprints-container');
    const allContainer = document.getElementById('all-publications-container');

    if (!featuredContainer && !preprintContainer && !allContainer) {
        return;
    }

    fetch(getDataPath('publications.json'))
        .then(handleJsonResponse)
        .then(publications => {
            if (featuredContainer) {
                const accepted = publications
                    .filter(pub => String(pub.type || '').toLowerCase() === 'accepted')
                    .sort(compareAllPublications);
                renderFeaturedPublications(featuredContainer, accepted);
            }

            if (preprintContainer) {
                const preprints = publications
                    .filter(pub => String(pub.type || '').toLowerCase() !== 'accepted')
                    .sort(compareAllPublications);
                renderFeaturedPublications(preprintContainer, preprints);
            }

            if (allContainer) {
                renderAllPublicationsPage(allContainer, publications);
            }
        })
        .catch(error => {
            console.error('Error loading publications data:', error);
            const container = featuredContainer || preprintContainer || allContainer;
            if (container) {
                container.innerHTML = '<p>Failed to load publications.</p>';
            }
        });
}

function renderFeaturedPublications(container, publications) {
    container.innerHTML = '';

    if (!publications.length) {
        container.innerHTML = '<p>No featured publications available.</p>';
        return;
    }

    const list = document.createElement('ul');
    list.className = 'pub-list-ul';

    publications.forEach(pub => {
        list.appendChild(createPublicationItem(pub));
    });

    container.appendChild(list);
}

function renderAllPublicationsPage(container, publications) {
    const filter = getPublicationFilter();
    const filterIndicator = document.getElementById('filter-indicator');

    let filtered = publications.slice();

    if (filter === 'first-author') {
        filtered = filtered.filter(pub => pub.isFirstAuthor === true);
        if (filterIndicator) {
            filterIndicator.textContent = '(First Author)';
        }
    } else if (filter === 'accepted') {
        filtered = filtered.filter(pub => String(pub.type || '').toLowerCase() === 'accepted');
        if (filterIndicator) {
            filterIndicator.textContent = '(Accepted)';
        }
    } else if (filter === 'preprint') {
        filtered = filtered.filter(pub => String(pub.type || '').toLowerCase() !== 'accepted');
        if (filterIndicator) {
            filterIndicator.textContent = '(Preprints)';
        }
    } else if (filterIndicator) {
        filterIndicator.textContent = '';
    }

    updateFilterButtons(filter);
    renderAllPublications(container, filtered);
}

function renderAllPublications(container, publications) {
    container.innerHTML = '';

    if (!publications.length) {
        container.innerHTML = '<p class="empty-state">No publications found for this filter.</p>';
        return;
    }

    const grouped = new Map();

    publications
        .slice()
        .sort(compareAllPublications)
        .forEach(pub => {
            const yearLabel = getYearLabel(pub);
            if (!grouped.has(yearLabel)) {
                grouped.set(yearLabel, []);
            }
            grouped.get(yearLabel).push(pub);
        });

    Array.from(grouped.entries()).forEach(([year, items]) => {
        const group = document.createElement('div');
        group.className = 'pub-year-group';

        const header = document.createElement('h2');
        header.className = 'pub-year-header';
        header.textContent = year;
        group.appendChild(header);

        const list = document.createElement('ul');
        list.className = 'pub-list-ul';
        items.forEach(pub => {
            list.appendChild(createPublicationItem(pub));
        });

        group.appendChild(list);
        container.appendChild(group);
    });
}

function createPublicationItem(pub) {
    const simplePage = document.body.matches('.homepage-simple, .academic-simple');
    const item = document.createElement('li');
    item.className = simplePage ? 'pub-list-item' : 'pub-list-item with-thumbnail-expanded';

    const content = document.createElement('div');
    content.className = 'pub-content-wrapper';

    const line1 = document.createElement('div');
    line1.className = 'pub-line-1';

    const title = document.createElement('span');
    title.className = 'pub-title-text';
    title.textContent = pub.displayTitle || pub.title || 'Untitled Publication';
    line1.appendChild(title);
    content.appendChild(line1);

    const line2 = document.createElement('div');
    line2.className = 'pub-line-2';
    line2.innerHTML = pub.authors || '';
    content.appendChild(line2);

    const line3 = document.createElement('div');
    line3.className = 'pub-line-3';

    const venueFullName = getVenueFullName(pub.venue, pub.year);
    const venueShortName = getVenueShortName(pub.venue, pub.year);
    const venueText = venueFullName || pub.venue || 'Preprint';

    const venueNameSpan = document.createElement('span');
    venueNameSpan.textContent = venueText;
    line3.appendChild(venueNameSpan);

    if (shouldShowVenueTag(pub.venue, venueFullName, venueShortName)) {
        const venueTag = document.createElement('span');
        venueTag.className = 'pub-venue-tag pub-venue-inline-tag';
        venueTag.textContent = venueShortName;

        const lowerVenue = venueShortName.toLowerCase();
        if (lowerVenue.includes('under review') || lowerVenue.includes('preprint') || lowerVenue.includes('arxiv')) {
            venueTag.classList.add('tag-under-review');
        } else {
            venueTag.classList.add('tag-conference');
        }

        line3.appendChild(venueTag);
    }

    const badgeText = getHighlightBadge(pub.highlight);
    if (badgeText) {
        const badge = document.createElement('span');
        badge.className = 'pub-badge-highlight';
        badge.textContent = badgeText;
        line3.appendChild(badge);
    }

    content.appendChild(line3);

    if (pub.tags && Array.isArray(pub.tags)) {
        const line4 = document.createElement('div');
        line4.className = 'pub-line-4';

        pub.tags.forEach(tag => {
            const label = tag.text === 'Paper' ? 'PDF' : (tag.text || 'Link');
            const usableLink = hasUsableLink(tag.link);

            const button = document.createElement(usableLink ? 'a' : 'span');
            button.className = 'pub-link-btn';
            button.textContent = label;

            if (usableLink) {
                button.href = normalizeAssetPath(tag.link);
                button.target = '_blank';
                button.rel = 'noopener noreferrer';
            } else {
                button.classList.add('is-placeholder');
                button.title = 'Replace "#" with a real link in data/publications.json';
            }

            line4.appendChild(button);
        });

        if (line4.children.length > 0) {
            content.appendChild(line4);
        }
    }

    item.appendChild(content);

    if (pub.thumbnail && !simplePage) {
        const thumbBox = document.createElement('div');
        thumbBox.className = 'pub-thumbnail-box';

        const thumbImg = document.createElement('img');
        const preferredThumbnail = getPreferredThumbnail(pub.thumbnail);
        thumbImg.src = preferredThumbnail.primary;
        thumbImg.alt = `${pub.title || 'Publication'} preview`;
        thumbImg.loading = 'lazy';
        thumbImg.onerror = function() {
            if (this.src !== preferredThumbnail.fallback) {
                this.onerror = null;
                this.src = preferredThumbnail.fallback;
            }
        };

        thumbBox.appendChild(thumbImg);
        item.appendChild(thumbBox);
    }

    return item;
}

function renderNewsItems(newsData, container) {
    container.innerHTML = '';

    newsData.forEach(newsItem => {
        const newsElement = document.createElement('div');
        newsElement.className = 'news-item';

        const dateElement = document.createElement('span');
        dateElement.className = 'news-date';
        dateElement.textContent = newsItem.date || '';

        const contentElement = document.createElement('div');
        contentElement.className = 'news-content';

        const textSpan = document.createElement('span');
        const prefix = document.body.matches('.homepage-simple, .academic-simple') ? '' : '🎉 ';
        textSpan.innerHTML = prefix + (newsItem.content || '');
        contentElement.appendChild(textSpan);

        if (Array.isArray(newsItem.links)) {
            newsItem.links.forEach(link => {
                const space = document.createTextNode(' ');
                contentElement.appendChild(space);

                const anchor = document.createElement('a');
                anchor.href = normalizeAssetPath(link.url || '#');
                anchor.textContent = link.text || 'Link';
                if (shouldOpenInNewTab(anchor.getAttribute('href'))) {
                    anchor.target = '_blank';
                    anchor.rel = 'noopener noreferrer';
                }
                contentElement.appendChild(anchor);
            });
        }

        newsElement.appendChild(dateElement);
        newsElement.appendChild(contentElement);
        container.appendChild(newsElement);
    });
}

function renderHonorsItems(honorsData, container) {
    container.innerHTML = '';

    honorsData.forEach(honorItem => {
        const honorElement = document.createElement('div');
        honorElement.className = 'honor-item';

        const yearElement = document.createElement('div');
        yearElement.className = 'honor-year';
        yearElement.textContent = honorItem.date || '';

        const contentElement = document.createElement('div');
        contentElement.className = 'honor-content';

        const titleElement = document.createElement('h3');
        titleElement.textContent = honorItem.title || '';
        contentElement.appendChild(titleElement);

        const descElement = document.createElement('p');
        if (honorItem.description) {
            descElement.innerHTML = honorItem.description;
        } else {
            descElement.textContent = honorItem.org || '';
        }
        contentElement.appendChild(descElement);

        honorElement.appendChild(yearElement);
        honorElement.appendChild(contentElement);
        container.appendChild(honorElement);
    });
}

function compareFeaturedPublications(a, b) {
    const orderA = a.featuredOrder ?? Number.MAX_SAFE_INTEGER;
    const orderB = b.featuredOrder ?? Number.MAX_SAFE_INTEGER;
    if (orderA !== orderB) {
        return orderA - orderB;
    }
    return compareAllPublications(a, b);
}

function compareAllPublications(a, b) {
    const yearA = getComparableYear(a);
    const yearB = getComparableYear(b);
    if (yearA !== yearB) {
        return yearB - yearA;
    }

    const acceptedA = String(a.type || '').toLowerCase() === 'accepted' ? 1 : 0;
    const acceptedB = String(b.type || '').toLowerCase() === 'accepted' ? 1 : 0;
    if (acceptedA !== acceptedB) {
        return acceptedB - acceptedA;
    }

    const orderA = a.featuredOrder ?? Number.MAX_SAFE_INTEGER;
    const orderB = b.featuredOrder ?? Number.MAX_SAFE_INTEGER;
    if (orderA !== orderB) {
        return orderA - orderB;
    }

    return String(a.title || '').localeCompare(String(b.title || ''));
}

function getComparableYear(pub) {
    const parsedYear = parseInt(pub.year, 10);
    if (!Number.isNaN(parsedYear)) {
        return parsedYear;
    }
    return String(pub.type || '').toLowerCase() === 'accepted' ? 0 : 9999;
}

function getYearLabel(pub) {
    const parsedYear = parseInt(pub.year, 10);
    if (!Number.isNaN(parsedYear)) {
        return String(parsedYear);
    }
    return 'Preprints / Under Review';
}

function getPublicationFilter() {
    const params = new URLSearchParams(window.location.search);
    return params.get('filter') || 'all';
}

function updateFilterButtons(filter) {
    document.querySelectorAll('.filter-link').forEach(link => {
        link.classList.remove('active');
        link.removeAttribute('aria-current');
    });

    let activeId = 'filter-all';
    if (filter === 'first-author') {
        activeId = 'filter-first';
    } else if (filter === 'accepted') {
        activeId = 'filter-accepted';
    } else if (filter === 'preprint') {
        activeId = 'filter-preprint';
    }
    const element = document.getElementById(activeId);
    if (element) {
        element.classList.add('active');
        element.setAttribute('aria-current', 'page');
    }
}

function getHighlightBadge(highlightText) {
    const text = String(highlightText || '').toLowerCase();
    if (text.includes('oral')) {
        return 'Oral';
    }
    if (text.includes('spotlight')) {
        return 'Spotlight';
    }
    return '';
}

function getPreferredThumbnail(thumbnailPath) {
    const lastSlash = thumbnailPath.lastIndexOf('/');
    if (lastSlash === -1) {
        const normalized = normalizeAssetPath(thumbnailPath);
        return { primary: normalized, fallback: normalized };
    }

    const directory = thumbnailPath.substring(0, lastSlash);
    return {
        primary: normalizeAssetPath(`${directory}/demo.gif`),
        fallback: normalizeAssetPath(thumbnailPath)
    };
}

function getVenueShortName(venueStr, year) {
    if (!venueStr) {
        return 'Preprint';
    }

    let revisionSuffix = '';
    if (venueStr.toLowerCase().includes('major revision')) {
        revisionSuffix = ', Major';
    } else if (venueStr.toLowerCase().includes('minor revision')) {
        revisionSuffix = ', Minor';
    }

    let s = venueStr.replace(/\d{4}/g, '').trim();
    let suffix = '';

    const conferences = ['NeurIPS', 'ICML', 'ICLR', 'EMNLP', 'ACL', 'CVPR', 'ICCV', 'ECCV', 'ICRA', 'AAAI', 'GLOBECOM', 'INFOCOM', 'MOBICOM'];
    for (const conf of conferences) {
        if (s.includes(conf)) {
            if (year) {
                const yearStr = String(year);
                if (yearStr.length === 4) {
                    suffix = "'" + yearStr.substring(2);
                }
            }
            return conf + suffix + revisionSuffix;
        }
    }

    if (s.toLowerCase().includes('arxiv')) {
        return 'ArXiv' + revisionSuffix;
    }

    if (s.includes('TMLR')) return 'TMLR' + revisionSuffix;

    if (s.includes('TDSC')) return 'IEEE TDSC' + revisionSuffix;
    if (s.includes('TMC')) return 'IEEE TMC' + revisionSuffix;
    if (s.includes('JSAC')) return 'IEEE JSAC' + revisionSuffix;
    if (s.includes('TGCN')) return 'IEEE TGCN' + revisionSuffix;
    if (s.includes('LNET')) return 'IEEE LNET' + revisionSuffix;
    if (s.includes('TNSE')) return 'IEEE TNSE' + revisionSuffix;
    if (s.includes('IOTJ') || s.includes('IoTJ')) return 'IEEE IoTJ' + revisionSuffix;

    return s || 'Preprint';
}

function getVenueFullName(venueStr) {
    if (!venueStr) {
        return '';
    }

    const s = venueStr.replace(/\d{4}/g, '').trim();

    if (s.includes('TDSC')) return 'IEEE Transactions on Dependable and Secure Computing';
    if (s.includes('TMC')) return 'IEEE Transactions on Mobile Computing';
    if (s.includes('JSAC')) return 'IEEE Journal on Selected Areas in Communications';
    if (s.includes('TGCN')) return 'IEEE Transactions on Green Communications and Networking';
    if (s.includes('TNSE')) return 'IEEE Transactions on Network Science and Engineering';
    if (s.includes('IoTJ') || s.includes('IOTJ')) return 'IEEE Internet of Things Journal';
    if (s.includes('LNET') || s.includes('LNet')) return 'IEEE Networking Letters';

    if (s.includes('NeurIPS')) return 'Annual Conference on Neural Information Processing Systems';
    if (s.includes('ICML')) return 'International Conference on Machine Learning';
    if (s.includes('CVPR')) return 'IEEE/CVF Conference on Computer Vision and Pattern Recognition';
    if (s.includes('ICCV')) return 'IEEE/CVF International Conference on Computer Vision';
    if (s.includes('ECCV')) return 'European Conference on Computer Vision';
    if (s.includes('ICRA')) return 'IEEE International Conference on Robotics and Automation';
    if (s.includes('AAAI')) return 'AAAI Conference on Artificial Intelligence';
    if (s.includes('GLOBECOM')) return 'IEEE Global Communications Conference';
    if (s.includes('INFOCOM')) return 'IEEE International Conference on Computer Communications';
    if (s.includes('MOBICOM')) return 'Annual International Conference on Mobile Computing and Networking';

    if (s.includes('ICLR')) return 'International Conference on Learning Representations';
    if (s.includes('EMNLP')) return 'Conference on Empirical Methods in Natural Language Processing';
    if (s.includes('ACL')) return 'Annual Meeting of the Association for Computational Linguistics';
    if (s.includes('TMLR')) return 'Transactions on Machine Learning Research';

    if (s.toLowerCase().includes('arxiv')) return 'arXiv preprint';

    return s;
}

function shouldShowVenueTag(venueStr, fullVenueName, venueShort) {
    if (!venueShort) {
        return false;
    }

    const shortLower = venueShort.toLowerCase().trim();
    const fullLower = String(fullVenueName || '').toLowerCase().trim();

    if (!fullLower || shortLower === fullLower) {
        return false;
    }

    if (venueStr && venueStr.toLowerCase().includes('under review')) {
        return false;
    }

    return true;
}

function getDataPath(fileName) {
    const base = window.location.pathname.includes('/pages/') ? `../data/${fileName}` : `data/${fileName}`;
    return `${base}?t=${Date.now()}`;
}

function normalizeAssetPath(path) {
    if (!path) {
        return path;
    }

    if (/^(https?:|mailto:|tel:|#)/i.test(path)) {
        return path;
    }

    if (window.location.pathname.includes('/pages/') && !path.startsWith('../')) {
        return `../${path}`;
    }

    return path;
}

function hasUsableLink(path) {
    return Boolean(path) && path !== '#';
}

function handleJsonResponse(response) {
    if (!response.ok) {
        throw new Error(`Request failed: ${response.status}`);
    }
    return response.json();
}

function makeAllLinksOpenInNewTab() {
    document.querySelectorAll('a').forEach(link => {
        const href = link.getAttribute('href');
        if (shouldOpenInNewTab(href)) {
            link.target = '_blank';
            link.rel = 'noopener noreferrer';
        }
    });
}

function shouldOpenInNewTab(href) {
    if (!href) {
        return false;
    }
    // Only external (absolute) URLs open in a new tab; all relative/in-page
    // links (including filtered .html?query links) stay in the same tab.
    if (/^(https?:)?\/\//i.test(href)) {
        return true;
    }
    return false;
}

function setupLinkObserver() {
    if (!document.body) {
        return;
    }

    const observer = new MutationObserver(mutations => {
        let shouldRefreshLinks = false;

        for (const mutation of mutations) {
            if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                shouldRefreshLinks = true;
                break;
            }
        }

        if (shouldRefreshLinks) {
            makeAllLinksOpenInNewTab();
        }
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
}
